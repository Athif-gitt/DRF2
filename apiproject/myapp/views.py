from rest_framework.response import Response
from rest_framework.views import APIView
from .services import fetch_external_data

class ExternalApiView(APIView):
    def get(self, request):
        token = request.headers.get("Authorization")

        if not token:
            return Response(
                {"error": "Authorization header missing"},
                status=401
            )

        data = fetch_external_data(token)
        return Response(data)

