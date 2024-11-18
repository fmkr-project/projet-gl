from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifie si l'utilisateur n'est pas connecté
        if not request.user.is_authenticated:
            # Exclut certaines URLs (comme login et logout)
            exempt_urls = [settings.LOGIN_URL, settings.LOGOUT_REDIRECT_URL]
            if not any(request.path.startswith(url) for url in exempt_urls):
                # Redirige vers la page de login
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        # Passe la requête au middleware suivant ou à la vue
        return self.get_response(request)
