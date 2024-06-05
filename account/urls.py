from django.urls import path

from account.views import AccountListView, AccountCreateView, CurrencyUpdateView

app_name = "account"

urlpatterns = [
    path("", AccountListView.as_view(), name="account-list"),
    path("currency/<int:pk>", CurrencyUpdateView.as_view(), name="currency"),
    path("create/", AccountCreateView.as_view(), name="account-create"),
]
