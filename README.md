# phone-restful-api
This is a restful API development by Python


# Overview & Goal
The goal of this exercise is to create a standalone application exposing a REST/HTTP interface according to the requirements below.


# Requirements
Create an /v1/phone-numbers endpoint that takes request parameters and returns information about a phone number.


# Programming Language
I used Python to implement this Restful-API


# Library and Framework
- flask-restful: 

Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. https://flask-restful.readthedocs.io/en/latest/index.html

- phonenumbers: 

Python version of Google's common library for parsing, formatting, storing and validating international phone numbers. https://pypi.org/project/phonenumbers/

- phone-iso3166: 

Small project to map an E.164 (international) phone number to the ISO-3166-1 alpha 2 (two letter) country code, associated with that number.  https://pypi.org/project/phone-iso3166/

- pycountry: 

ISO country, subdivision, language, currency and script definitions and their translations. https://pypi.org/project/pycountry/

- requests: 

Python HTTP for Humans. https://pypi.org/project/requests/

  
# Install
  After built the python environment, execute the following in terminal.
  
- pip install requests
- pip install flask-restful
- pip install pycountry
- pip install phone-iso3166
- pip install phonenumbers


# Procedure for handling a program startup error

If the following error occurs, when start the /src/phone_api.py.

```diff
- Error "from itsdangerous import json as _json ImportError: cannot import name 'json' from 'itsdangerous'"
```

Fix itsdangerous version to 2.0.1 by 

pip install itsdangerous==2.0.1

Reference: https://serverfault.com/questions/1094062/error-from-itsdangerous-import-json-as-json-importerror-cannot-import-name-j


# Run

- Run Rest Server
  - https://github.com/Yuehao-Wang/phone-restful-api/blob/main/src/phone_api.py is the Server. Run it in python environment.

- Unit Test
  - https://github.com/Yuehao-Wang/phone-restful-api/blob/main/src/phone_test.py is the unit test. Run it in python environment.
  
- Test samples

After the Rest server started (phone_api.py is running), We can browse following links in Chrome, and FireFox
  - http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B12125690123

  - http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=631%20311%208150

  - http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B52%20631%203118150

  - http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=34%20915%20872200

  - http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=351%2021%20094%20%20%202000

- Samples of result
  - success:
  {
    "phoneNumber": "+12125690123",
    "countryCode": "US",
    "areaCode": "212",
    "localPhoneNumber": "5690123"
  }
  
  - error:
 {
    "phoneNumber": "+1212569012",
    "error": {
        "countryCode": "required value is missing"
    }
  }
  
  
# Explanation of how you would deploy to production.
We can use third-party tools or webhooks of Github to deploy code.

- When the test environment passes, it can be deployed to the production environment
- push codes to production trunk
- the github send a upgrading request to the production server.
- After the production server received the upgrading request, it excutes the auto-deployment script. 网站服务器收到更新请求，执行自动部署脚本
- The auto-deployment script would pull codes, package, and deploy


# Explanation of assumptions you ma
- Assumption 1: The length of phone is no more than 15
- Assumption 2: Only accept +, space, and digit in the string of phone number
- Assumption 3: The first digit must be 1 - 9

# Explanation of improvements you wish to make
- The program should handle more phone formats
  - +14255551212 (Implemented)
  - +1 (425) 555-1212 (Wait for the implementation)
  - +1 425-555-1212 (Wait for the implementation)
  - +1-425-555-1212 (Wait for the implementation)
  - +1 425.555.1212 (Wait for the implementation)

