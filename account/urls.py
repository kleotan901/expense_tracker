
from django.urls import path

from account.views import AccountListView

app_name = "account"

urlpatterns = [
    path("", AccountListView.as_view(), name="account-list"),
]