from .views import EmailView, LoginView, RegistrationView
from django.urls import path


app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("send-simple-email/", EmailView.as_view(), name="simple_email"),
]
