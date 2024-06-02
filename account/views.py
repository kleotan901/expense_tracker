from django.views import generic

from account.models import Account


class AccountListView(generic.ListView):
    model = Account
    template_name = "account/accounts.html"
    paginate_by = 5
