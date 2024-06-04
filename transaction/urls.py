from django.contrib import admin
from django.urls import path

from transaction.views import (
    AllTransactionsView,
    ExpenseListView,
    IncomeListView,
    CategoryCreateView,
    CategoryListView,
    ExpenseCreateView,
    IncomeCreateView,
)

app_name = "transaction"

urlpatterns = [
    path("", AllTransactionsView.as_view(), name="all-transactions"),
    path("expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("incomes/", IncomeListView.as_view(), name="income-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("category/create/", CategoryCreateView.as_view(), name="category-create"),
    path("expenses/create/", ExpenseCreateView.as_view(), name="expense-create"),
    path("incomes/create/", IncomeCreateView.as_view(), name="income-create"),
]
