from django.urls import path
from . import views


urlpatterns = [
    # Sets the url path to home page index.html
    path('', views.home, name='index'),
    # Sets the url path to create new account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    # Sets the url path to Balance sheet page BalanceSheet.html.
    path('balance/', views.balance, name='balance'),
    # Sets the url path tp add new transaction page AddNewTransaction.html.
    path('transaction/', views.transaction, name='transaction')
]