from django.test import TestCase
from ..models import NewsSubscription, ContactForm
from django.urls import reverse


class HomePageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')


class AboutPageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/about.html')


class ServicesPageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:services'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/services.html')


class PortfolioPageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:portfolio'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/portfolio.html')


class PricePageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:price'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/price.html')


class BlogHomePageTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:bloghome'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/blog-home.html')


class PageViewTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:pages'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/elements.html')


class ContactViewTests(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')


class EmailTest(TestCase):

    def setUp(self):
        self.news = NewsSubscription.objects.create(news_email='pablo@esebesoftware.com')
        self.create_url = reverse('portfolio:sendmail')

    def test_send_email(self):
        response = self.client.post(self.create_url, data={

            'email': ['pablo@esebesoftware.com'],

        })

        self.assertEquals(response.status_code, 200)


class SendMailTest(TestCase):

    def test_create_success_url(self):
        url = reverse('portfolio:sendmail')
        self.client.post(url,
                         {

                             'email': [''],

                         }
                         )


class ContactTest(TestCase):

    def setUp(self):
        self.author = ContactForm.objects.create(name='ali', email='pablo@esebesoftware.com', subject='my name',
                                                 message="hii")
        self.create_url = reverse('portfolio:contactmessage')

    def test_contact(self):
        response = self.client.post(self.create_url, data={
            'name': 'ali',
            'email': ['pablo@esebesoftware.com'],
            'subject': 'my name',
            'message': 'hii'

        })

        self.assertEquals(response.status_code, 200)
