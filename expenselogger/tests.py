"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from datetime import date
from expenselogger.models import Expense

class SimpleTest(TestCase):
    def setUp(self):
        Expense(name = "Joe", type = "Flight", amount=100, date = date.today())
        Expense(name = "Bob", type = "Hotel", amount=233, date = date.today())

    def expenses(self):
        joe = Expense.objects.get(name="Joe")
        bob = Expense.objects.get(name="Bob")
        self.assertEqual(joe.name, "Joe")
        self.assertEqual(joe.type, "Flight")
        self.assertEqual(joe.amount, 100)
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.type, "Hotel")
        self.assertEqual(bob.amount, 233)