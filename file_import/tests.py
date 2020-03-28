from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


class PagesTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
       

    def test_find_page_status_code(self):
        response = self.client.get('/find/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')

    def test_view_uses_correct_template2(self):
        response = self.client.get(reverse('find'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'find.html')


    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h2 style = "position:relative;  top: 110px;">Выберите csv.файл</h2>')

    def test_find_page_contains_correct_html(self):
        response = self.client.get('/find/')
        self.assertContains(response, '<h2>Поиск сотрудников</h2>')
