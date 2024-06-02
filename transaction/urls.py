from django.contrib import admin
from django.urls import path

from transaction.views import AllTransactionsView

app_name = "transaction"

urlpatterns = [
    path("", AllTransactionsView.as_view(), name="all-transactions"),
]
