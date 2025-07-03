import uuid
import requests
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Transaction
from .models import Transaction
User = get_user_model()

# Allow GET logout
class AllowGetLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'paymentapp/transactions.html', {'transactions': transactions})

# Home Page View
def home(request):
    return render(request, 'paymentapp/home.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'paymentapp/register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'paymentapp/login.html'

    def get_success_url(self):
        return '/payment/pay/'

# Optional custom logout view using GET
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Square API Integration (Sandbox)
def process_square_payment(amount):
    url = "https://connect.squareupsandbox.com/v2/payments"

    headers = {
        "Authorization": f"Bearer {settings.SQUARE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "idempotency_key": str(uuid.uuid4()),
        "amount_money": {
            "amount": int(amount * 100),  # dollars to cents
            "currency": "USD"
        },
        "source_id": "cnon:card-nonce-ok",  # sandbox test nonce
        "location_id": "LN3EZG10NE33Z"     # your sandbox location ID
    }

    return requests.post(url, headers=headers, json=body)

# Payment View
@login_required
def make_payment(request):
    if request.method == 'GET':
        return render(request, 'paymentapp/pay.html')

    elif request.method == 'POST':
        try:
            amount = float(request.POST.get('amount', 0))
            api_response = process_square_payment(amount)
            data = api_response.json()

            if api_response.status_code == 200 and data.get("payment"):
                payment = data["payment"]
                Transaction.objects.create(
                    user=request.user,
                    payment_id=payment["id"],
                    order_id=payment["id"],
                    amount=payment["amount_money"]["amount"] / 100,
                    currency=payment["amount_money"]["currency"],
                    status=payment["status"],
                    created_at=timezone.now()
                )
                return redirect(reverse('payment_confirmation', kwargs={
                    'status': 'success'
                }) + f"?id={payment['id']}&amount={payment['amount_money']['amount'] / 100}")
            else:
                error_detail = data.get("errors", [{}])[0].get("detail", "Unknown error")
                return redirect(reverse('payment_confirmation', kwargs={
                   'status': 'failed'
                }) + f"?error={error_detail}&amount={amount}")

        except Exception as e:
            return redirect(reverse('payment_confirmation', kwargs={
               'status': 'failed'
            }) + f"?error={str(e)}&amount={amount}")


def payment_confirmation(request, status):
    payment_id = request.GET.get('id', '')
    amount = request.GET.get('amount', '')
    error = request.GET.get('error', '')

    return render(request, 'paymentapp/confirmation.html', {
        'status': status,
        'payment_id': payment_id,
        'amount': amount,
        'error': error
    })
