from django.urls import reverse_lazy
from django.views import generic

from account.currency_exchange import get_accounts_balance
from account.models import Account, Currency


class CurrencyUpdateView(generic.UpdateView):
    model = Currency
    fields = "__all__"
    success_url = reverse_lazy("transaction:all-transactions")
    template_name = "account/currency_settings.html"


class AccountListView(generic.ListView):
    model = Account
    template_name = "account/accounts.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        accounts = Account.objects.all()
        context["total_accounts_balance"] = get_accounts_balance(accounts)
        context["currency"] = Currency.objects.get(id=1)

        return context


class AccountCreateView(generic.CreateView):
    model = Account
    fields = ["account_type", "balance", "currency"]
    success_url = reverse_lazy("account:account-list")
    template_name = "account/account_form.html"
