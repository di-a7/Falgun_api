from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedorReadOnly(BasePermission):
   def has_permission(self, request, view):
      if request.method in SAFE_METHODS or request.user and request.user.is_authenticated:
         return True