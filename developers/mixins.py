from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OwnerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an owner."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_owner:
            return redirect("issues:issue-list")
        return super().dispatch(request, *args, **kwargs)