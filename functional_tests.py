# -*- coding: utf-8 -*-
from selenium import webdriver
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
        self.fail('Finish the test!')
        
        # �׳��� �ٷ� �۾��� �߰��ϱ��� �Ѵ�.
        
        # "���۱��� ����"���� �ؽ�Ʈ ���ڿ� �Է��Ѵ�
        # (�������� ���̴� ��ġ ���̿� �׹��� ������ ���̴�)
        
        # ����Ű�� ġ�� �������� ���ŵǰ� �۾� ���Ͽ�
        # "1: ���۱��� ����" �������� �߰��ȴ�
        
        # �߰� �������� �Է��� �� �ִ� ������ �ؽ�Ʈ ���ڰ� �����Ѵ�
        # �ٽ� "���۱����� �̿��ؼ� �׹� ������"���� �Է��Ѵ�. (���𽺴� �ſ� ü������ �����̴�.)
        
        # �������� �ٽ� ���ŵǰ�, �� �� �������� ���Ͽ� ���δ�
        # ���𽺴� ����Ʈ�� �Է��� ������ �����ϰ� �ִ��� �ñ��ϴ�
        # ����Ʈ�� �׳ฦ ���� Ư�� URL�� �������ش�
        # �̶� URL�� ���� ������ �Բ� �����Ѵ�
        
        # �ش� URL�� �����ϸ� �׳డ ���� �۾� ������ �״��� �ִ� ���� Ȯ���� �� �ִ�.
        
        # �����ϰ� ���ڸ��� ����
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
