from django.shortcuts import render
from django.views import generic

from transaction.models import Expense, Income


class AllTransactionsView(generic.ListView):
    template_name = "transaction/transactions.html"
    context_object_name = "transactions"
    paginate_by = 5

    def get_queryset(self):
        incomes = Income.objects.all()
        expenses = Expense.objects.all()

        transactions = []

        for income in incomes:
            transactions.append(
                {
                    "date": income.date,
                    "amount": income.amount,
                    "description": income.description,
                    "category": income.category,
                    "type": "income",
                }
            )

        for expense in expenses:
            transactions.append(
                {
                    "date": expense.date,
                    "amount": expense.amount,
                    "description": expense.description,
                    "category": expense.category,
                    "type": "expense",
                }
            )

        transactions.sort(
            key=lambda x: x["date"], reverse=True
        )
        return transactions


class ExpenseListView(generic.ListView):
    model = Expense
    paginate_by = 5


class IncomeListView(generic.ListView):
    model = Income
    paginate_by = 5
