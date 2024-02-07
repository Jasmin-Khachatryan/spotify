from django.shortcuts import redirect, render
from functools import wraps


def profile_decorator(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.user.pk != kwargs.get("pk"):
            return redirect("home:home")
        return func(*args, **kwargs)
    return wrapper


def premium_user_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_premium_user:

            return render(request, "music/card.html")
        return func(request, *args, **kwargs)

    return wrapper

# def pro_user_required(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         if not request.user.is_premium_user:
#             return render(request, "music/card.html")
#         return func(request, *args, **kwargs)
#
#     return wrapper
