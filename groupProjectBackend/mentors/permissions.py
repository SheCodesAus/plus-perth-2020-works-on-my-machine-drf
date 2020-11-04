from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

# class IsAdminUserOrReadOnly(IsAdminUser):

#     def has_permission(self, request, view):
#         is_admin = super(
#             IsAdminUserOrReadOnly, 
#             self).has_permission(request, view)
#         # Python3: is_admin = super().has_permission(request, view)
#         return request.method in SAFE_METHODS or is_admin

# class IsStaffOrReadOnly(permissions.BasePermission):
    
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.owner == request.user.user_type(staff)

class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
