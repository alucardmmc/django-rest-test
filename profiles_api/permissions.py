from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allows an user to edit his profile """

    def has_object_permission(self, request, view, obj):
        """ Checks if the user is trying to edit his own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """ Allows own user feed update """

    def has_object_permission(self, request, view, obj):
        """ Check if the user is trying to edit his own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile_id == request.user.id

