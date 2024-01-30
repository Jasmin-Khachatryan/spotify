from django.shortcuts import redirect
from functools import wraps


def profile_decorator(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.user.pk != kwargs.get("pk"):
            return redirect("home:home")
        return func(*args, **kwargs)
    return wrapper
