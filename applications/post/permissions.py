from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    
    # def has_permission(self, request, view):
    #     return super().has_permission()

    def has_object_permission(self, request, view, obj):
        print(request.method)
        print(SAFE_METHODS)
        if request.method == "GET":
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user == obj. owner or request.user.is_staff
# True and admin2admin == john@gmail.com
