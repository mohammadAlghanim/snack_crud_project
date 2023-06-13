from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snacks


class SnackTests(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester",password="tester")
        Snacks.objects.create(name="rake", purchaser=reviewer)

    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        things = response.context['snacks']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "rake")
        self.assertEqual(things[0].description, 'bla bla bla ..')
        self.assertEqual(things[0].purchaser.username, "tester")
    
    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        thing = response.context['snacks']
        self.assertEqual(thing.name, "rake")
        self.assertEqual(thing.description, 'bla bla bla ..')
        self.assertEqual(thing.purchaser.username, "tester")
