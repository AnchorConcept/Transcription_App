from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": (
            "Welcome to Aurum API. Go to /api/transcriptions/ or "
            "/api/auth/token/"
        )
    })
