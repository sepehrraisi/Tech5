from django.shortcuts import redirect
from django.urls import reverse


class AuthenticatedUserMixin:
    """
        This decorator redirect authenticated users to main page.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('core:home'))
        return super().dispatch(request, *args, **kwargs)
