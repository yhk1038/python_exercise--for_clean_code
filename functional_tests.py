# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # ������(Edith)�� �����۾����Ͽ¶��ξ��̳��Դٴ¼ҽ��� ����
        # �ش� �� ����Ʈ�� Ȯ���Ϸ� ����
        self.browser.get('http://localhost:8000')
        
        # �� ������ Ÿ��Ʋ�� ������ 'To-Do'�� ǥ���ϰ� �ִ�.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # �׳��� �ٷ� �۾��� �߰��ϱ��� �Ѵ�.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )
        
        # "���۱��� ����"���� �ؽ�Ʈ ���ڿ� �Է��Ѵ�
        # (�������� ���̴� ��ġ ���̿� �׹��� ������ ���̴�)
        inputbox.send_keys('공작깃털 사기')
        
        # ����Ű�� ġ�� �������� ���ŵǰ� �۾� ���Ͽ�
        # "1: ���۱��� ����" �������� �߰��ȴ�
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
        )
        
        # �߰� �������� �Է��� �� �ִ� ������ �ؽ�Ʈ ���ڰ� �����Ѵ�
        # �ٽ� "���۱����� �̿��ؼ� �׹� ������"���� �Է��Ѵ�. (���𽺴� �ſ� ü������ �����̴�.)
        self.fail('Finish the test!')
        
        # �������� �ٽ� ���ŵǰ�, �� �� �������� ���Ͽ� ���δ�
        # ���𽺴� ����Ʈ�� �Է��� ������ �����ϰ� �ִ��� �ñ��ϴ�
        # ����Ʈ�� �׳ฦ ���� Ư�� URL�� �������ش�
        # �̶� URL�� ���� ������ �Բ� �����Ѵ�
        
        # �ش� URL�� �����ϸ� �׳డ ���� �۾� ������ �״��� �ִ� ���� Ȯ���� �� �ִ�.
        
        # �����ϰ� ���ڸ��� ����
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
