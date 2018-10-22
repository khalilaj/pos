from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


class ResourceDoesNotExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Resource does not exist'


def core_exception_handler(exc, context):

    err = exception_handler(exc, context)

    handlers = {"Http404": handle_not_found, "AuthenticationFailed": handle_generic}

    err_class = exc.__class__.__name__

    if err_class in handlers:
        return handlers[err_class](exc, context, err)

    return err


def handle_generic(exc, context, err):

    print({"d": err.data})

    return err


def handle_not_found(exc, context, err):

    err.data = {
        "errors": err.data["detail"],
        "status_code": err.status_code,
        "ip": context["request"].META["REMOTE_ADDR"],
    }

    return err


class UserNotAllowed(APIException):
    pass
