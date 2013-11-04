from expenselogger.models import Expense
from django.shortcuts import render

def index(request):
    
    #grab expenses from database and display them
    expense_list = []
    for e in Expense.objects.raw('SELECT * FROM expenselogger_expense'):
        expense_list.insert(0, e) #insert at top of the list

    context = {'expense_list': expense_list}
    return render(request, 'expenselogger/index.html', context)
    
def create_expense(request):
    #create an expense and add it to the database
    try:
        content = request.POST["expense_name"]
        amount = request.POST["expense_amount"]
        date = request.POST["expense_date"]
        etype = request.POST["expense_type"]
        e = Expense(name = content, type = etype, amount=amount, date = date)
        e.save()
        return index(request)
    #if no expense was created, just call main page
    except:
        return index(request)

