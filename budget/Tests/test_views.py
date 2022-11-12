from django.test import TestCase , Client
from django.urls import reverse
from budget.models import *
import json

class TestViews(TestCase):
    def test_project_list_GET(self):
        client= Client()
        response= client.get(reverse('list'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'budget/project-list.html')
        
    def test_project_detial_GET(self):
        Project.objects.create(
            name="project1",
            budget=1000
        )
        client= Client()
        response= client.get(reverse('detail',args=['project1']))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'budget/project-detail.html')
#############################################
    def test_project_detial_POST_adds_new_expense(self):
        self.project1=Project.objects.create(
            name="project1",
            budget=1000
        ) 
        Category.objects.create(
                project=self.project1,
                name='devloppment'
            )
        client= Client()

        response= client.post(reverse('detail',args=['project1']),{
                'title':'expense1',
                'amount':1000,
                'category':'devloppment'
            })
        self.assertEquals(response.status_code,302)
        self.assertEquals(self.project1.expenses.first().title,'expense1')
###############################################
    def test_project_detial_DELETE_expense(self):
        self.project1=Project.objects.create(
            name="project1",
            budget=1000
        ) 
        cat=Category.objects.create(
                project=self.project1,
                name='devloppment'
            )
        Expense.objects.create(
                project=self.project1,
                title='expenses1',
                amount=1000,
                category=cat
            )
        client= Client()

        response= client.delete(reverse('detail',args=['project1']),json.dumps({
                'id':'1' 
            }))
        self.assertEquals(response.status_code,204)
        self.assertEquals(self.project1.expenses.count(),0)    
        ##############no Id
        
    def test_project_detial_DELETE_expense_no_id(self):
        self.project1=Project.objects.create(
            name="project1",
            budget=1000
        ) 
        cat=Category.objects.create(
                project=self.project1,
                name='devloppment'
            )
        Expense.objects.create(
                project=self.project1,
                title='expenses1',
                amount=1000,
                category=cat
            )
        client= Client()

        response= client.delete(reverse('detail',args=['project1']))
        self.assertEquals(response.status_code,404)
        self.assertEquals(self.project1.expenses.count(),1)    
            

        
        
