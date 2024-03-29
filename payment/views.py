import stripe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from .models import Account

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(ListView):
    model = Account

    template_name = "payment/payment.html"
    context_object_name = "payments"


def create_checkout_session(request, pk):
    account = Account.objects.get(pk=pk)
    price_id = None
    if account.name == "Pro Students":
        price_id = 'price_1Oc2UsKkfxRy5FMrFrxexWkz'
    elif account.name == "Pro Account":
        price_id = 'price_1Oc2OHKkfxRy5FMrLnedflLG'
    else:
        price_id = 'price_1Ob707KkfxRy5FMruheltV7K'

    session_id = request.GET.get('session_id')

    user = request.user

    if account.name in ["Pro Students", "Pro Account", "Premium Account"]:
        user.is_premium_user = True
        user.account = account
        user.save()

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('payment:success')),
        cancel_url=request.build_absolute_uri(reverse('payment:cancel')),
    )
    account.stripe_session_id = session.id
    account.save()

    return redirect(session.url, code=303)


@method_decorator(login_required, name='dispatch')
class SuccessView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        user = request.user

        if not user.is_premium_user:
            messages.error(request, 'Sorry. You are not authorized to view this page.')
            return redirect("home:home")

        messages.success(request, 'Thank you. Your payment was successfully processed and your premium status is now active!')

        return redirect("home:home")


class CancelView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        user = request.user
        if not user.is_premium_user:
            messages.error(request, 'Sorry. You are not authorized to view this page.')
            return redirect("home:home")

        messages.error(request, 'Sorry. Your payment was canceled!')
