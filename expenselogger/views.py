from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.core.context_processors import csrf

def index(request):
    expsense_list = []  #implement me
    context = {'expense_list': expsense_list}
    return render(request, 'expenselogger/index.html', context)
    
def create_expense(request):
    content = request.POST["expense_name"]
    amount = request.POST["expense_amount"]
    date = request.POST["expense_date"]
    e = Expense(name = content, type = "Flight", amount=amount, date = date)
    e.save()
    expsense_list = []  #implement me
    context = {'expense_list': expsense_list}
    return render(request, 'expenselogger/index.html', context)

