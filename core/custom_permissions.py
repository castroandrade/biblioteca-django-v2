from rest_framework import permissions

# Passo 1.5 -  arquivo custom_permissions.py com a permissão para que apenas o colecionador possa modificar sua coleção
class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Todos os usuários podem ler (GET, HEAD ou OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Apenas o colecionador pode editar ou excluir
        return obj.colecionador == request.user