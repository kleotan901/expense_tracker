from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect

from django.urls import reverse_lazy, reverse
from django.views import generic

from account.forms import AccountForm, UserAccountCreateForm, UserCurrencyUpdateForm
from account.models import Account, Currency, UserAccount


class UserCreateView(generic.CreateView):
    model = UserAccount
    form_class = UserAccountCreateForm
    template_name = "account/user_form.html"
    success_url = reverse_lazy("accounts:account-list")


class UserCurrencyUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserCurrencyUpdateForm
    success_url = reverse_lazy("transaction:all-transactions")
    template_name = "account/currency_settings.html"

    def get_object(self, *args, **kwargs):
        return self.request.user # Return the current logged-in user


class AccountListView(LoginRequiredMixin, generic.ListView):
    model = Account
    template_name = "account/accounts.html"
    #login_url = "registration/login.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        accounts_of_user = Account.objects.filter(user=self.request.user)
        context["total_accounts_balance"] = accounts_of_user.aggregate(
            total=Sum("converted_balance")
        )["total"]
        base_currency_of_user = self.request.user.currency_id.code
        context["currency"] = Currency.objects.get(code=base_currency_of_user)

        return context

    # Only owner can see his/her own accounts
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class AccountCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = AccountForm
    success_url = reverse_lazy("account:account-list")
    template_name = "account/account_form.html"

    # The logged-in user saved to DB as the account owner
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Account
    success_url = reverse_lazy("account:account-list")
    template_name = "account/account_delete_confirmation.html"
