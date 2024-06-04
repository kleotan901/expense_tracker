from django.urls import reverse_lazy
from django.views import generic

from account.forms import AccountForm
from account.models import Account


class AccountListView(generic.ListView):
    model = Account
    template_name = "account/accounts.html"
    paginate_by = 5


class AccountCreateView(generic.CreateView):
    form_class = AccountForm
    success_url = reverse_lazy("account:account-list")
    template_name = "account/account_form.html"
