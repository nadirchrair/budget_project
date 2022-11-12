from django.test import TestCase
from budget.models import Project , Category, Expense
class TestModels(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            name= 'project-1',
            budget = 10000
        )
    def test_if_nameproject_assignd_slug(self):
        self.assertEquals(self.project1.slug , 'project-1')    
    def test_budget_left(self):
        category1 = Category.objects.create(
            project =self.project1,
            name='devlopmment'
        )
        Expense.objects.create(
            project =self.project1,
            title = 'expense1',
            amount = 1000,
            category=category1
 
        )
        Expense.objects.create(
            project =self.project1,
            title = 'expense2',
            amount = 2000,
            category=category1
 
        )
        self.assertEquals(self.project1.budget_left , 7000)

    def total_transactions_test(self):
        self.project2 = Project.objects.create(
            name= 'project-2',
            budget = 10000
        )
        category1 = Category.objects.create(
            project =self.project2,
            name='conception'
        )
        Expense.objects.create(
            project =self.project2,
            title = 'expense1',
            amount = 4000,
            category=category1
 
        )
        Expense.objects.create(
            project =self.project2,
            title = 'expense2',
            amount = 2000,
            category=category1
 
        )
        self.assertEquals(self.project1.total_transactions , 2)
