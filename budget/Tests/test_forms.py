from django.test import SimpleTestCase
from budget.forms import ExpenseForm
class TestForms(SimpleTestCase):
    def test_Expenseforms(self):
        form = ExpenseForm(data={
            'title' : 'expese',
            'amount' : 1000 ,
            'category' : 'conception'          
        })
        self.assertTrue(form.is_valid())
    def test_Expenseforms_invalid(self):
        form = ExpenseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)
