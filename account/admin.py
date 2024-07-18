from django.contrib import admin

from account.models import UserAccount, Account

admin.site.register(UserAccount)
admin.site.register(Account)
