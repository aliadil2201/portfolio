from django.test import TestCase
from ..models import Personal, Qualification, Designation, LatestProjectFeatures, MyOfferedServices, ServicesComplete, \
    Blog, ClientFeedbackAboutMe, ChosePlan, QuestionAnswer, BlogHomeBanner, BlogHomeCategoryWidget, BlogHomeContent, \
    BlogHomeSearchPost, BlogHomeCategory, BlogSinglePost, BlogSingleComment, BlogSingleLeaveComment, NewsSubscription, \
    ContentFormAddressInfo, ContactForm, BlogHomePopularPost


class EntryModelTest(TestCase):

    def test_return(self):
        entry = Personal(Name="Ali")
        self.assertEqual(str(entry), entry.Name)


class QualificationModelTest(TestCase):

    def test_return(self):
        entry = Qualification(degree_name="mcs")
        self.assertEqual(str(entry), entry.degree_name)


class DesignationModelTest(TestCase):

    def test_return(self):
        entry = Designation(post="professor")
        self.assertEqual(str(entry), entry.post)


class LatestProjectFeaturesModelTest(TestCase):

    def test_return(self):
        test = LatestProjectFeatures(title='English')
        self.assertEqual(str(test), test.title)


class MyOfferedServicesModelTest(TestCase):

    def test_return(self):
        test = MyOfferedServices(Name='Ali')
        self.assertEqual(str(test), test.Name)


class ServicesCompleteModelTest(TestCase):

    def test_return(self):
        test = ServicesComplete(services_title='xyz')
        self.assertEqual(str(test), test.services_title)


class BlogModelTest(TestCase):

    def test_return(self):
        test = Blog(user_name='English')
        self.assertEqual(str(test), test.user_name)


class ClientFeedbackAboutMeModelTest(TestCase):

    def test_return(self):
        test = ClientFeedbackAboutMe(client_name='Ali')
        self.assertEqual(str(test), test.client_name)


class ChosePlanModelTest(TestCase):

    def test_return(self):
        test = ChosePlan(package_name='Xyz')
        self.assertEqual(str(test), test.package_name)


class QuestionAnswerModelTest(TestCase):

    def test_return(self):
        test = QuestionAnswer(question='how are you?')
        self.assertEqual(str(test), test.question)


class BlogHomePopularPostModelTest(TestCase):
    def test_return(self):
        test = BlogHomePopularPost(name='ali')
        self.assertEqual(str(test), test.name)


class BlogHomeBannerModelTest(TestCase):

    def test_return(self):
        test = BlogHomeBanner(title='English')
        self.assertEqual(str(test), test.title)


class BlogHomeCategoryWidgetModelTest(TestCase):

    def test_return(self):
        test = BlogHomeCategoryWidget(category_title='politics')
        self.assertEqual(str(test), test.category_title)


class BlogHomeContentModelTest(TestCase):

    def test_return(self):
        test = BlogHomeContent(blog_title='politics')
        self.assertEqual(str(test), test.blog_title)

    def test_return_summary(self):
        test = BlogHomeContent(blog_description='')
        self.assertEqual(str(test), test.blog_description[:200])


class BlogHomeSearchPostModelTest(TestCase):

    def test_return(self):
        test = BlogHomeSearchPost(name='politics')
        self.assertEqual(str(test), test.name)


class BlogHomeCategoryModelTest(TestCase):

    def test_return(self):
        test = BlogHomeCategory(category_name='politics')
        self.assertEqual(str(test), test.category_name)


class BlogSinglePostModelTest(TestCase):

    def test_return(self):
        test = BlogSinglePost(description='politics')
        self.assertEqual(str(test), test.description)


class BlogSingleCommentModelTest(TestCase):

    def test_return(self):
        test = BlogSingleComment(name='Ali')
        self.assertEqual(str(test), test.name)


class BlogSingleLeaveCommentModelTest(TestCase):

    def test_return(self):
        test = BlogSingleLeaveComment(enter_name='politics')
        self.assertEqual(str(test), test.enter_name)


class NewsSubscriptionModelTest(TestCase):

    def test_return(self):
        test = NewsSubscription(news_email='pabl@esebesoftware.com')
        self.assertEqual(str(test), test.news_email)


class ContentFormAddressInfoModelTest(TestCase):

    def test_return(self):
        test = ContentFormAddressInfo(state_address='xyz')
        self.assertEqual(str(test), test.state_address)


class ContactFormModelTest(TestCase):

    def test_return(self):
        test = ContactForm(name='form')
        self.assertEqual(str(test), test.name)

