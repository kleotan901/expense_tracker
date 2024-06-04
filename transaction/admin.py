from django.contrib import admin

from transaction.models import Category, Expense, Income

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)
