import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserRegister, LoginHistory


@csrf_exempt
def register_user(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        name = data.get("name")
        phone = data.get("phone")
        password = data.get("password")

        if not name or not phone or not password:
            return JsonResponse({"error": "All fields required"}, status=400)

        if UserRegister.objects.filter(phone=phone).exists():
            return JsonResponse({"message": "User already exists"})

        UserRegister.objects.create(
            name=name,
            phone=phone,
            password=password
        )

        return JsonResponse({"message": "Registration Successful"})

    return JsonResponse({"error": "Invalid request"}, status=405)


@csrf_exempt
def login_user(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        phone = data.get("phone")
        password = data.get("password")

        if not phone or not password:
            return JsonResponse({"error": "Phone & Password required"}, status=400)

        user = UserRegister.objects.filter(phone=phone).first()

        if not user:
            return JsonResponse({
                "message": "Phone number not registered"
            })

        if user.password != password:
            return JsonResponse({
                "message": "Wrong password"
            })

        # save login history
        LoginHistory.objects.create(user=user)

        return JsonResponse({
            "message": "Login Successful",
            "name": user.name
        })

    return JsonResponse({"error": "Invalid request"}, status=405)