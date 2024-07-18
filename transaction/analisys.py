import numpy as np
import pandas as pd
from django.db.models import Sum
from pandas import DataFrame

from transaction.models import Category, Expense


def retrieve_transactions_by_month() -> [dict]:
    categories = Category.objects.select_related().annotate(
        total_sum=Sum("expense__converted_amount")
    )
    expense_transactions = {}
    income_transactions = {}
    for category in categories:
        for expense in category.expense_set.all():
            if expense.date in expense_transactions:
                expense_transactions[expense.date.month] += expense.amount
            else:
                expense_transactions[expense.date.month] = expense.amount
        for income in category.income_set.all():
            if income.date in income_transactions:
                income_transactions[income.date.month] += income.amount
            else:
                income_transactions[income.date.month] = income.amount

    return expense_transactions, income_transactions


def convert_to_dataframe() -> DataFrame:
    expense_transactions = retrieve_transactions_by_month()[0]
    income_transactions = retrieve_transactions_by_month()[1]
    # Creating DataFrames from dictionaries
    df_expense = pd.DataFrame(
        list(expense_transactions.items()), columns=["month", "expense"]
    )
    df_income = pd.DataFrame(
        list(income_transactions.items()), columns=["month", "income"]
    )

    df_transactions = pd.merge(df_expense, df_income, on="month", how="outer").fillna(0)
    df_transactions["expense"] = df_transactions["expense"].astype(float)
    df_transactions["income"] = df_transactions["income"].astype(float)

    # Converting month number to a datetime object for better sorting
    df_transactions["month"] = (
        pd.to_datetime(df_transactions["month"], format="%m")
        .dt.month_name()
        .str.slice(stop=3)
    )
    # Grouping by month and summing up expenses and income
    df_transactions = (
        df_transactions.groupby("month")
        .agg({"expense": "sum", "income": "sum"})
        .reset_index()
    )
    # Sorting months in chronological order
    months_ordered = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    df_transactions["month"] = pd.Categorical(
        df_transactions["month"], categories=months_ordered, ordered=True
    )
    df_transactions = df_transactions.sort_values("month")
    return df_transactions


def get_data_expense_analisys() -> DataFrame:
    expense_sum_by_categories = Category.objects.select_related().annotate(
        total_sum=Sum("expense__converted_amount")
    )
    data_list = []
    categories_name = []
    for category in expense_sum_by_categories:
        if category.total_sum:
            data_list.append(float(category.total_sum))
            categories_name.append(category.name)

    df_expenses = pd.DataFrame({"category": categories_name, "amount": data_list})
    return df_expenses


def get_data_income_analisys() -> DataFrame:
    income_sum_by_categories = Category.objects.select_related().annotate(
        total_sum=Sum("income__converted_amount")
    )
    data_list = []
    categories_name = []
    for category in income_sum_by_categories:
        if category.total_sum:
            data_list.append(float(category.total_sum))
            categories_name.append(category.name)
    df_income = pd.DataFrame({"category": categories_name, "amount": data_list})
    return df_income


def to_percent(pct, all_values):
    absolute = int(np.round(pct / 100.0 * np.sum(all_values)))
    return f"{pct:.2f}%\n({absolute})"
