from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import register, CustomLoginView, make_payment, transaction_list, home
from .views import AllowGetLogoutView
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', AllowGetLogoutView.as_view(), name='logout'),
    path('pay/', make_payment, name='make_payment'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('pay/', views.make_payment, name='make_payment'),
    path('confirmation/<str:status>/', views.payment_confirmation, name='payment_confirmation'),
]



 
 
