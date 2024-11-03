from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from django.views.decorators.http import require_POST

# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "account/login.html",
                {"error": "Kullanıcı adı veya şifre hatalı"},
            )

    return render(request, "account/login.html")


# @require_POST # sadece post isteklerini kabul eder
# def login_request(request):
#     username = request.POST["username"]
#     password = request.POST["password"]

#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("home")
#     else:
#         return render(
#             request,
#             "account/login.html",
#             {"error": "Kullanıcı adı veya şifre hatalı"},
#         )


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]

        if password != repassword:
            return render(
                request,
                "account/register.html",
                {
                    "error": "Şifreler uyuşmuyor",
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                },
            )
        if User.objects.filter(username=username).exists():
            return render(
                request,
                "account/register.html",
                {
                    "error": "Kullanıcı adı kullanılıyor",
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                },
            )
        if User.objects.filter(email=email).exists():
            return render(
                request,
                "account/register.html",
                {
                    "error": "Email kullanılıyor",
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                },
            )
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
            email=email,
        )

        return redirect("login")
    return render(request, "account/register.html")


def logout_request(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("home")
