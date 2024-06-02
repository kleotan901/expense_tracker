from django.contrib import admin
from django.urls import path

from transaction.views import AllTransactionsView, ExpenseListView, IncomeListView

app_name = "transaction"

urlpatterns = [
    path("", AllTransactionsView.as_view(), name="all-transactions"),
    path("expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("incomes/", IncomeListView.as_view(), name="income-list"),
]
