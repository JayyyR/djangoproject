from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.core.context_processors import csrf
import pdb

def index(request):
    expense_list = []  #implement me
    for e in Expense.objects.raw('SELECT * FROM expenselogger_expense'):
        expense_list.insert(0, e)
        print(e.date)
    
    for e in expense_list:
        print(e.amount)
    context = {'expense_list': expense_list}
    return render(request, 'expenselogger/index.html', context)
    
def create_expense(request):
    try:
        content = request.POST["expense_name"]
        amount = request.POST["expense_amount"]
        date = request.POST["expense_date"]
        etype = request.POST["expense_type"]
        e = Expense(name = content, type = etype, amount=amount, date = date)
        e.save()
        return index(request)
    except:
        return index(request)

