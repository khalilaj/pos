from rest_framework.exceptions import APIException


class NoProductsKey(APIException):
    status_code = 430
    default_detail = "No Products Key Provided"
    default_code = "email-not-given"
