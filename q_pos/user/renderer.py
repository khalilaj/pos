import json
from ..core.renderer import QuickieRenderer


class AccountRenderer(QuickieRenderer):
    object_name = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        """
        1. Checks to see if their errors in the data
        2. It Sets the token on the data if None
        3. If token is present decode the token

        :return:  json dumps of the user object with the token attribute
        :rtype: A json object
        """

        if 'errors' in data:
            return super(AccountRenderer, self).render(data)

        token = data['token'] if 'token' in data else None

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({self.object_name:data})
