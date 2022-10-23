from flask import Flask, request
from flask_restful import Resource, Api
from phone_iso3166.country import phone_country
import phonenumbers as phonenumbers_api

app = Flask(__name__)
api = Api(app)


def validate_number(phone_num):
    res = {
        "phoneNumber": phone_num
    }
    err = {}

    if len(phone_num) > 15:
        err["check error"] = "the length is must <= 15"
        res["error"] = err
        return res

    # remove all space
    phone_num.strip()
    phone_num = ''.join(phone_num.split())

    # remove the first +, if it is existed.
    if phone_num[0] == "+":
        phone_num = phone_num[1:]

    if phone_num[0] < "1" or phone_num[0] > "9":
        err["phoneNumber"] = "the first character must be 1 - 9"
        res["error"] = err
        return res

    # are all digit?
    for i in range(len(phone_num)):
        if not phone_num[i].isdigit():
            err["phoneNumber"] = "the character " + phone_num[i] + " is allowed"
            res["error"] = err
            return res

    if len(phone_num) < 7:
        err["localPhoneNumber"] = "required value is missing"
        err["areaCode"] = "required value is missing"
        err["countryCode"] = "required value is missing"
        res["error"] = err
        return res

    if len(phone_num) < 10 and len(phone_num) >= 7:
        err["areaCode"] = "required value is missing"
        err["countryCode"] = "required value is missing"
        res["error"] = err
        return res

    if len(phone_num) < 11 and len(phone_num) >= 10:
        err["countryCode"] = "required value is missing"
        res["error"] = err
        return res

    if len(phone_num) >= 11 and phone_num[0] != "+":
        phone_num = "+" + phone_num

    try:
        check_phone_number = phonenumbers_api.parse(phone_num, None)
    except Exception as e:
        err["check error"] = "is invalid phone number"
        res["error"] = err
        return res

    if not phonenumbers_api.is_possible_number(check_phone_number):
        err["check error"] = "is not a possible number"
        res["error"] = err
        return res

    if not phonenumbers_api.is_valid_number(check_phone_number):
        err["check error"] = "is not a valid number"
        res["error"] = err
        return res

    country_code = ""
    try:
        country_code = phone_country(phone_num)
    except Exception as e:
        err["check error"] = "is invalid country code"
        res["error"] = err
        return res

    local_phone_number = phone_num[-7:]
    area_code = phone_num[-10:-7]

    res["countryCode"] = country_code
    res["areaCode"] = area_code
    res["localPhoneNumber"] = local_phone_number

    return res


# the Restful interface
class phone_numbers(Resource):

    def get(self):
        phoneNumber = request.args.get("phoneNumber")

        validate_result = validate_number(phoneNumber)

        return validate_result


api.add_resource(phone_numbers, '/v1/phone-numbers', endpoint='phone-numbers')

if __name__ == '__main__':
    app.run(debug=True)