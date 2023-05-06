from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOnly(BasePermission):
    """
    Доступ только у пользователя с ролью администратор или суперпользователь.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает анонимному пользователю только безопасные запросы.
    Полный доступ у авторизованнорго пользователя с ролью
    администратор.
    """
    message = 'Доступ только у администратора.'

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated and request.user.is_admin))


class AdminModeratorAuthorPermission(BasePermission):
    """
    Разрешает анонимному пользователю только безопасные запросы.
    Все остальные запросы разрешаются авторизованному пользователю.
    Доступ к объекту имеют пользователи с ролью администратор,
    суперпользователь или модератор, а также автор объекта.
    """
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )
