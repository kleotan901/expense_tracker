from django.db.models import Sum
from django.urls import reverse_lazy
from django.views import generic

from account.currency_exchange import get_total_amount, get_accounts_balance
from account.models import Account, Currency

from transaction.forms import CategoryForm, ExpenseForm, IncomeForm
from transaction.models import Expense, Income, Category


class AllTransactionsView(generic.ListView):
    template_name = "transaction/transactions.html"
    context_object_name = "transactions"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AllTransactionsView, self).get_context_data(**kwargs)
        incomes = Income.objects.all()
        expenses = Expense.objects.all()
        account_balance = Account.objects.all()
        context["total_income_sum"] = get_total_amount(incomes)
        context["total_expense_sum"] = get_total_amount(expenses)
        context["account_balance"] = get_accounts_balance(account_balance)
        # Проверяем, являются ли значения None, если да, то присваиваем им значение 0
        total_expense_sum = context["total_expense_sum"] if context["total_expense_sum"] is not None else 0
        total_income_sum = context["total_income_sum"] if context["total_income_sum"] is not None else 0
        account_balance_sum = context["account_balance"] if context["account_balance"] is not None else 0

        context["balance"] = (
                total_income_sum
                - total_expense_sum
                + account_balance_sum
        )

        context["currency"] = Currency.objects.get(id=1)

        return context

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
                    "account_currency": income.account.currency
                }
            )

        for expense in expenses:
            transactions.append(
                {
                    "date": expense.date,
                    "amount": expense.amount,
                    "description": expense.description,
                    "category": expense.category,
                    "account_currency": expense.account.currency
                }
            )

        transactions.sort(key=lambda x: x["date"], reverse=True)
        return transactions


class ExpenseListView(generic.ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        expenses = Expense.objects.all()
        context["total_expense_sum"] = get_total_amount(expenses)
        context["currency"] = Currency.objects.get(id=1)

        return context


class IncomeListView(generic.ListView):
    model = Income
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        income = Income.objects.all()
        context["total_income_sum"] = get_total_amount(income)
        context["currency"] = Currency.objects.get(id=1)

        return context


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5


class CategoryCreateView(generic.CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy("transaction:category-list")
    template_name = "transaction/category_form.html"


class ExpenseCreateView(generic.CreateView):
    form_class = ExpenseForm
    success_url = reverse_lazy("transaction:expense-list")
    template_name = "transaction/expense_form.html"


class IncomeCreateView(generic.CreateView):
    form_class = IncomeForm
    success_url = reverse_lazy("transaction:income-list")
    template_name = "transaction/income_form.html"
