from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
       if request.user.groups.filter(name='Managers').exists():
            return True

class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
       if request.user.groups.filter(name='Delivery crew').exists():
            return True

