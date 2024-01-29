from .views import LoginView, RegistrationView, LogoutView, UserProfileView, UserUpdateView, ValidateUserLink
from django.urls import path


app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("<int:pk>/<str:token>/", ValidateUserLink.as_view(), name="verify"),
    path("logout/", LogoutView.as_view(), name="Logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("edit-profile/<int:pk>/", UserUpdateView.as_view(), name="edit_profile"),

]
