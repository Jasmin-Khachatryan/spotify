import stripe
<<<<<<< Updated upstream

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

=======
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.views.generic import ListView,TemplateView
from django.contrib import messages
from .models import Account
stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(ListView):
    model = Account

    template_name = "payment/payment.html"
    context_object_name = "payments"


>>>>>>> Stashed changes
def create_checkout_session(request, pk):
    account = Account.objects.get(pk=pk)
    price_id = None

    if account.name == "Pro Students":
        price_id = 'price_1Oc2UsKkfxRy5FMrFrxexWkz'
    elif account.name == "Pro Account":
        price_id = 'price_1Oc2OHKkfxRy5FMrLnedflLG'
    else:
        price_id = 'price_1Ob707KkfxRy5FMruheltV7K'

<<<<<<< Updated upstream
    session_id = request.GET.get('session_id')

    user = request.user
    user.account = account
    user.is_premium_user = True
    user.save()

=======
>>>>>>> Stashed changes
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='subscription',
<<<<<<< Updated upstream
        success_url=request.build_absolute_uri(reverse('payment:success')),
=======
        success_url=request.build_absolute_uri(reverse('home:home')),
>>>>>>> Stashed changes
        cancel_url=request.build_absolute_uri(reverse('payment:cancel')),
    )

    account.stripe_session_id = session.id
    account.save()

    return redirect(session.url, code=303)

<<<<<<< Updated upstream
@method_decorator(login_required, name='dispatch')
=======
>>>>>>> Stashed changes
class SuccessView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
<<<<<<< Updated upstream
        user = request.user

        if not user.account in ["Pro Students", "Pro Account", "Premium Account", ]:
            messages.success(request, 'Thank you. Your payment was successfully processed and your premium status is now active!')
            return redirect("home:home")

        messages.error(request, 'Sorry. You are not authorized to view this page.')

        return redirect("home:home")
=======
        if session_id:
            messages.success(request, 'Thank you. Your payment was successfully processed!')
        return super().get(request, *args, **kwargs)
>>>>>>> Stashed changes

class CancelView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
<<<<<<< Updated upstream
        user = request.user
        if not user.is_premium_user:
            messages.error(request, 'Sorry. You are not authorized to view this page.')
            return redirect("home:home")

        messages.error(request, 'Sorry. Your payment was canceled!')

        return redirect("home:home")
=======
        if session_id:
            messages.success(request, 'Sory. Your payment was canceld!')
        return super().get(request, *args, **kwargs)
>>>>>>> Stashed changes
