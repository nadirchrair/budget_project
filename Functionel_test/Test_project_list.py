from selenium import webdriver
from budget.models import   Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import     TestCase
import time
from selenium.webdriver.common.by import By

class TestProjectListPage(StaticLiveServerTestCase):
    def tearDown(self):
        self.browser = webdriver.Chrome('Functionel_test/chromedriver.exe')

        self.browser.close()    
        
    
    def test_no_project_alert_is_displayed(self):
        self.browser = webdriver.Chrome('Functionel_test/chromedriver.exe')
        self.browser.get(self.live_server_url)   
        alert = self.browser.find_element(By.CLASS_NAME, 'noproject-wrapper')
        self.assertEquals(
            alert.find_element(By.TAG_NAME, 'h3').text,
            'Sorry, you don\'t have any projects, yet.'
        )
   #def test_no_project_alert_button_redirect_to_add_page(self):
    #        self.browser = webdriver.Chrome('Functionel_test/chromedriver.exe')
     #       add_url = self.live_server_url + reverse('add')
      #      self.browser.find_element(By.TAG_NAME, 'a').click()       
       #     self.assertEquals(
        #    self.browser.current_url,
         #   add_url
        #)'''
 
