from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST["item_text"] = "신규 작업 아이템"
        response = home_page(request)
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        # self.assertEqual(expected_html, response.content.decode())
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'
        
        response = home_page(request)
        
        self.assertIn('신규 작업 아이템', response.content.decode())
        
class ItemNodelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()
        
        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()
        
        saved_items = Item.objects.all()
        #saved_items에 2개가 잘 들어갔는지 check
        self.assertEqual(saved_items.count(), 2)    
        
        #saved_items를 배열로 봤을때 첫 object를 first_saved_item로 명명.
        first_saved_item = saved_items[0]           
        #saved_items를 배열로 봤을때 두번째 object를 second_saved_item로 명명.
        second_saved_item = saved_items[1]
        #각각 정의된 것들이 의도된대로 정의됐는지 check
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')