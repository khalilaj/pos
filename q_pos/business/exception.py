from rest_framework.exceptions import APIException


class NoEmailProvided(APIException):
    status_code = 430
    default_detail = "No email Provided"
    default_code = "email-not-given"


class UserNotFound(APIException):
    status_code = 440
    default_detail = "Incorrect Email or Password provided"
    default_code = "merchant-not-found"


class UserNotActive(APIException):
    status_code = 404
    default_detail = "Error"
    default_code = "merchant-not-active"
