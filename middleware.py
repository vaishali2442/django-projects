from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import AnonymousUser
from users.models import users
from jwt import decode as jwt_decode

class JWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)

        if auth_header is not None and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]

            try:
                # Validate the token & decode claims
                validated_token = UntypedToken(token)
                decoded_data = jwt_decode(
                    token,
                    api_settings.SIGNING_KEY,
                    algorithms=[api_settings.ALGORITHM]
                )

                # Example: you could attach claims to request
                request.jwt_payload = decoded_data

                # Example: you could set request.user
                user_id = decoded_data.get('user_id')
                user = users.objects.filter(user_id=user_id).first()
                if user:
                    request.user = user
                else:
                    request.user = AnonymousUser()

            except (InvalidToken, TokenError):
                request.user = AnonymousUser()

        else:
            request.user = AnonymousUser()
