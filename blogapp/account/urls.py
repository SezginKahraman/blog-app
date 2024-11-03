from django.urls import path
from . import views

# http://127.0.0.1:8000/blogs
# http://127.0.0.1:8000/blogs/3
urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
]
