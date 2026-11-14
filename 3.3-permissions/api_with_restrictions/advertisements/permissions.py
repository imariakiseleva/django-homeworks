from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешаем изменение объявлений только его автору."""

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user