from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permissions_codename = self.__get_model_permissions_codename(
            method=request.method,
            view=view)    

        if not model_permissions_codename:
            return False
        
        return request.user.has_perm(model_permissions_codename)
    
    def __get_model_permissions_codename(self, method, view):

        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suffix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None
    
    def __get_action_suffix(self, method):
        method_actions = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
            "HEAD": "view",
            "OPTIONS": "view"
        }
        return method_actions.get(method, "")