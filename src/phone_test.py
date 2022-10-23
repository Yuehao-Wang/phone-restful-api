import requests


def test1():
    resp = requests.get(url="http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B12125690123")
    test_1_except = b'{\n    "phoneNumber": "+12125690123",\n    "countryCode": "US",\n    "areaCode": "212",\n    "localPhoneNumber": "5690123"\n}\n'

    try:
        assert test_1_except == resp.content
    except AssertionError as e:
        print("test 1 fail")
        # print(resp.content)
        # raise
    else:
        print("test 1 pass")


def test2():
    resp2 = requests.get(url="http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=631%20311%208150")
    test_2_except = b'{\n    "phoneNumber": "631 311 8150",\n    "error": {\n        "countryCode": "required value is missing"\n    }\n}\n'

    try:
        assert test_2_except == resp2.content
    except AssertionError as e:
        print("test 2 fail")
        # print(resp2.content)
        # raise
    else:
        print("test 2 pass")


def test3():
    resp3 = requests.get(url="http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B52%20631%203118150")
    test_3_except = b'{\n    "phoneNumber": "+52 631 3118150",\n    "countryCode": "MX",\n    "areaCode": "631",\n    "localPhoneNumber": "3118150"\n}\n'

    try:
        assert test_3_except == resp3.content
    except AssertionError as e:
        print("test 3 fail")
        # print(resp3.content)
        # raise
    else:
        print("test 3 pass")


def test4():
    resp4 = requests.get(url="http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=34%20915%20872200")
    test_4_except = b'{\n    "phoneNumber": "34 915 872200",\n    "countryCode": "ES",\n    "areaCode": "491",\n    "localPhoneNumber": "5872200"\n}\n'
    try:
        assert test_4_except == resp4.content
    except AssertionError as e:
        print("test 4 fail")
        # print(resp4.content)
        # raise
    else:
        print("test 4 pass")


def test5():
    resp5 = requests.get(url="http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=351%2021%20094%20%20%202000")
    test_5_except = b'{\n    "phoneNumber": "351 21 094   2000",\n    "error": {\n        "check error": "the length is must <= 15"\n    }\n}\n'
    try:
        assert test_5_except == resp5.content
    except AssertionError as e:
        print("test 5 fail")
        # print(resp5.content)
        # raise
    else:
        print("test 5 pass")


test1()
test2()
test3()
test4()
test5()
