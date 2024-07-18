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
    ExpenseDeleteView,
    IncomeDeleteView,
    CategoryDeleteView, dashboard,
)

app_name = "transaction"

urlpatterns = [
    path("", AllTransactionsView.as_view(), name="all-transactions"),
    path("dashboard/", dashboard, name="dashboard"),
    path("expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("incomes/", IncomeListView.as_view(), name="income-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("category/create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "category/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("expenses/create/", ExpenseCreateView.as_view(), name="expense-create"),
    path(
        "expenses/<int:pk>/delete/", ExpenseDeleteView.as_view(), name="expense-delete"
    ),
    path("incomes/create/", IncomeCreateView.as_view(), name="income-create"),
    path("incomes/<int:pk>/delete/", IncomeDeleteView.as_view(), name="income-delete"),
]
