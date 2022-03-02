import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

@api_view(['POST',])
@permission_classes((AllowAny,))
def login_view(request):
    """
    POST API for login
    """
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter username"
            }
        }, status=400)
    elif password is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter password"
            }
        }, status=400)

    # authentication user
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"success": "User has been logged in"})
    return JsonResponse(
        {"errors": "Invalid credentials"},
        status=400,
    )
