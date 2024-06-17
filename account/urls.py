from django.urls import path

from account.views import (
    AccountListView,
    AccountCreateView,
    UserCurrencyUpdateView,
    AccountDeleteView,
    UserCreateView,
)

app_name = "account"

urlpatterns = [
    path("", AccountListView.as_view(), name="account-list"),
    path("register", UserCreateView.as_view(), name="register"),
    path("update-currency/", UserCurrencyUpdateView.as_view(), name="update-currency"),
    path("create/", AccountCreateView.as_view(), name="account-create"),
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="account-delete"),
]
