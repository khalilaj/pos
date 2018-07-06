import jwt
from django.conf import settings

from rest_framework import authentication, exceptions

from ..user.models import Account


class JwtAuth(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """ Authenticates every request
        Args:
            request: Http request
        Return:
           A valid Account and token from the request header
           Exception raised when account is not active,
            account does not exist, token given is invalid
        """

        # Set the request.user to None
        request.user = None

        # Retrieve headers from request
        headers = authentication.get_authorization_header(request).split()

        prefix = self.authentication_header_prefix.lower()

        if not headers:
            return None

        if len(headers) == 1:
            return None

        if len(headers) > 2:
            return None

        header_prefix = headers[0].decode('utf-8')
        token = headers[1].decode('utf-8')

        if header_prefix.lower() != prefix:
            return None

        return authenticate_credentials(token)


def authenticate_credentials(token):
    """
    Decodes jwt token provided

    :param token: A jwt token
    :return:  A valid Account and the token arg
    :rtype: An Account object and token passed as arg
    """


    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
    except:
        err = "Authentication Failed"
        raise exceptions.AuthenticationFailed(err)

    try:
        account = Account.objects.get(pk=payload['id'])
    except Account.DoesNotExist:
        err = "Account not found"
        raise exceptions.AuthenticationFailed(err)

    if not account.is_active:
        err = "Account not active"
        raise exceptions.AuthenticationFailed(err)

    return account, token
