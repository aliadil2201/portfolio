from django.test import TestCase
from portfolio.forms import SendMailForm, SendMessageForm


class SaveFormTest(TestCase):

    data = {
        'news_email': 'pablo@esebesoftware.com',
    }

    def test_valid_form(self):
        form = SendMailForm(self.data)
        self.assertTrue(form.is_valid())


class SaveContactTest(TestCase):

    data = {
        'name': 'ali',
        'email': ['pablo@esebesoftware.com'],
        'subject': 'my name',
        'message': 'hii'
    }

    def test_valid_form(self):
        form = SendMessageForm(self.data)
        self.assertTrue(form.is_valid())
