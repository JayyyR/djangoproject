from expenselogger.models import Expense
from django.shortcuts import render

def index(request):
    expsense_list = []  #implement me
    context = {'expense_list': expsense_list}
    return render(request, 'expenselogger/index.html', context)
    
def create_expense(request):
    pass  # implement me
