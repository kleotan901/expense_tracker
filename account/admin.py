from django.contrib import admin

from account.models import Account, UserAccount

admin.site.register(UserAccount)
admin.site.register(Account)
