from django.test import SimpleTestCase
from django.urls import reverse , resolve
from budget.views import project_list , project_detail , ProjectCreateView
class TestUrls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        urls = reverse('list')
        self.assertEquals(resolve(urls).func,project_list )
    def test_add_urls_is_resolved(self):
        urls = reverse('add')
        self.assertEquals(resolve(urls).func.view_class,ProjectCreateView )    
    def test_detail_urls_is_resolved(self):
        urls = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(urls).func,project_detail )      