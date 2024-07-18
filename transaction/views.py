from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from django.urls import reverse_lazy
from django.views import generic

from account.models import Account, Currency

from transaction.forms import CategoryForm, ExpenseForm, IncomeForm
from transaction.models import Expense, Income, Category


class AllTransactionsView(LoginRequiredMixin, generic.ListView):
    template_name = "transaction/transactions.html"
    context_object_name = "transactions"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AllTransactionsView, self).get_context_data(**kwargs)
        context["currency"] = self.request.user.currency_id
        return context

    def get_queryset(self):
        expenses = Expense.objects.filter(account__user=self.request.user)
        incomes = Income.objects.filter(account__user=self.request.user)
        transactions = expenses.union(incomes).order_by('-date')
        return transactions


class ExpenseListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        expense_of_user = Expense.objects.filter(account__user=self.request.user)
        context["total_expense_sum"] = expense_of_user.aggregate(
            total=Sum("converted_amount")
        )["total"]
        base_currency_of_user = self.request.user.currency_id.code
        context["currency"] = Currency.objects.get(code=base_currency_of_user)

        return context

    def get_queryset(self):
        return Expense.objects.filter(account__user=self.request.user)


class IncomeListView(LoginRequiredMixin, generic.ListView):
    model = Income
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        income_of_user = Income.objects.filter(account__user=self.request.user)
        context["total_income_sum"] = income_of_user.aggregate(
            total=Sum("converted_amount")
        )["total"]
        base_currency_of_user = self.request.user.currency_id.code
        context["currency"] = Currency.objects.get(code=base_currency_of_user)

        return context

    def get_queryset(self):
        return Income.objects.filter(account__user=self.request.user)


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy("transaction:category-list")
    template_name = "transaction/category_form.html"

    # to add custom logic before saving to DB
    # this ensures that new category is linked to the user who is currently logged in
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy("transaction:category-list")
    template_name = "transaction/delete_confirmation.html"


class ExpenseCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ExpenseForm
    success_url = reverse_lazy("transaction:expense-list")
    template_name = "transaction/expense_form.html"

    # get_form_kwargs - adds the logged-in user to the form's keyword arguments
    # to pass the user as a keyword argument to ExpenseForm instance
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ExpenseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Expense
    success_url = reverse_lazy("transaction:expense-list")
    template_name = "transaction/delete_confirmation.html"


class IncomeCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = IncomeForm
    success_url = reverse_lazy("transaction:income-list")
    template_name = "transaction/income_form.html"

    # get_form_kwargs - adds the logged-in user to the form's keyword arguments
    # to pass the user as a keyword argument to IncomeForm instance
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class IncomeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Income
    success_url = reverse_lazy("transaction:income-list")
    template_name = "transaction/delete_confirmation.html"
