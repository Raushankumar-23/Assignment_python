from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostPossessor(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Read sabko allowed
        if request.method in SAFE_METHODS:
            return True

        # Edit/Delete sirf owner
        return obj.created_by == request.user