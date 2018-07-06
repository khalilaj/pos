from rest_framework import permissions


class MerchantAccessPermission(permissions.BasePermission):
    message = 'User not allowed.'

    def has_permission(self, request, view):

        account_type = request.user.user_type

        if request.method == 'GET':
            can_get = ['AD']
            return account_type in can_get

        elif request.method == 'POST':
            can_create = ['MC', 'AD']
            return account_type in can_create

        elif request.method == 'PUT':
            can_update = ['MC', 'AD']
            return account_type in can_update

        elif request.method == 'DELETE':
            can_delete = ['MC', 'AD']
            return account_type in can_delete
        else:
            return False