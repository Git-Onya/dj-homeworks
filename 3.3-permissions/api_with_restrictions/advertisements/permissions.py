from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator

class IsDraft(BasePermission):
    def has_object_permission(self, request, view, obj):
        a = obj.status
        if obj.status == 'DRAFT':
            return request.user == obj.creator
        return True
