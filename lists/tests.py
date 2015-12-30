from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, List
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
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        
        
class ListAndItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()
        
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.list = list_
        first_item.save()
        
        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.list = list_
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        saved_items = Item.objects.all()
        #saved_items에 2개가 잘 들어갔는지 check
        self.assertEqual(saved_items.count(), 2)    
        
        #saved_items를 배열로 봤을때 첫 object를 first_saved_item로 명명.
        first_saved_item = saved_items[0]
        #saved_items를 배열로 봤을때 두번째 object를 second_saved_item로 명명.
        second_saved_item = saved_items[1]
        #각각 정의된 것들이 의도된대로 정의됐는지 check
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
        self.assertEqual(second_saved_item.list, list_)
        
class ListViewTest(TestCase):
    
    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': '신규 작업 아이템'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')
        
    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'item_text': '신규 작업 아이템'}
        )
        self.assertRedirects(response, '/lists/the_only_list_in_the_world/')
    
    
    def test_users_list_template(self):
        response = self.client.get('/lists/the_only_list_in_the_world/')
        self.assertTemplateUsed(response, 'list.html')
    
    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)
        
        response = self.client.get('/lists/the_only_list_in_the_world/')
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')