from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import LatestProjectFeatures, MyOfferedServices, Blog, ClientFeedbackAboutMe, Personal, About, \
    ServicesComplete, \
    ChosePlan, ImageLabel, ToolExpertness, Qualification, Designation, QuestionAnswer, BlogHomeBanner, \
    BlogHomeCategoryWidget, \
    BlogHomeContent, BlogHomeSearchPost, BlogHomePopularPost, BlogHomeCategory, BlogHomeNewsLetter, BlogSinglePost, \
    BlogSingleComment, BlogSingleLeaveComment, BlogSingleTagsCloud, NewsSubscription, ContentFormAddressInfo, ContactForm
from django.views.generic import ListView


def sendmail(request):
    if request.method == 'POST':
        email = request.POST["email"]
        try:
            email = NewsSubscription.objects.get(news_email=request.POST['email'])
            return HttpResponse({'You are already Subscribed'})
        except:
            send_mal = NewsSubscription(news_email=email)
            send_mal.save()
            if request.method == 'POST':
                email = request.POST['email']
                from_email = settings.EMAIL_HOST_USER
                send_mail(subject='MedArt', message='Thank You for subscribing MedArt.', from_email=from_email,
                          recipient_list=[email], fail_silently=False)
            return HttpResponse({'You are Subscribed successfully'})
    # return HttpResponse('method not allowes', status=405)


class MyView(ListView):
    context_object_name = 'name'
    template_name = 'portfolio/index.html'
    queryset = LatestProjectFeatures.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['service'] = MyOfferedServices.objects.all()
        context['blog'] = Blog.objects.all()
        context['feature'] = LatestProjectFeatures.objects.all()
        context['feedback'] = ClientFeedbackAboutMe.objects.all()
        context['personal'] = Personal.objects.all()
        context['about'] = About.objects.all()
        context['complete_service'] = ServicesComplete.objects.all()
        context['chose_plan'] = ChosePlan.objects.all()
        context['label'] = ImageLabel.objects.all()
        return context


class AboutView(ListView):
    context_object_name = 'name'
    template_name = 'portfolio/about.html'
    queryset = About.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.objects.all()
        context['tool_expert'] = ToolExpertness.objects.all()
        context['qualification'] = Qualification.objects.all()
        context['designation'] = Designation.objects.all()
        context['feedback'] = ClientFeedbackAboutMe.objects.all()
        context['label'] = ImageLabel.objects.all()

        return context


class ServicesView(TemplateView):
    context_object_name = 'name'
    template_name = 'portfolio/services.html'
    queryset = MyOfferedServices.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['service'] = self.queryset
        context['complete_service'] = ServicesComplete.objects.all()
        context['chose_plan'] = ChosePlan.objects.all()
        context['feedback'] = ClientFeedbackAboutMe.objects.all()

        return context


class PortfolioView(ListView):
    context_object_name = 'name'
    template_name = 'portfolio/portfolio.html'
    queryset = LatestProjectFeatures.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['feature'] = self.queryset

        return context


class PriceView(TemplateView):
    context_object_name = 'name'
    template_name = 'portfolio/price.html'
    queryset = ChosePlan.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PriceView, self).get_context_data(**kwargs)
        context['chose_plan'] = self.queryset
        context['question_answer'] = QuestionAnswer.objects.all()
        return context


class BlogHomeView(TemplateView):
    context_object_name = 'name'
    template_name = 'portfolio/blog-home.html'
    queryset = BlogHomeBanner.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['blog_banner'] = self.queryset
        context['blog_category_widget'] = BlogHomeCategoryWidget.objects.all()
        context['blog_content'] = BlogHomeContent.objects.all()
        context['blog_search_post'] = BlogHomeSearchPost.objects.all()
        context['blog_popular_post'] = BlogHomePopularPost.objects.all()
        context['blog_home_category'] = BlogHomeCategory.objects.all()
        context['blog_home_newsletter'] = BlogHomeNewsLetter.objects.all()

        return context


class BlogSingleView(TemplateView):
    context_object_name = 'name'
    template_name = 'portfolio/blog-singl.html'


# class MyDetailView(DetailView):
#     model = BlogHomeContent
#     context_object_name = 'blog'
#     template_name = 'portfolio/blog-single.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MyDetailView, self).get_context_data(**kwargs)
#         context['blog_content'] = BlogHomeContent.objects.all()
#         context['blog_single_post'] = BlogSinglePost.objects.all()
#         context['blog_search_post'] = BlogHomeSearchPost.objects.all()
#         context['blog_popular_post'] = BlogHomePopularPost.objects.all()
#         context['blog_home_category'] = BlogHomeCategory.objects.all()
#         context['blog_home_newsletter'] = BlogHomeNewsLetter.objects.all()
#         context['blog_single_comment'] = BlogSingleComment.objects.all()
#         context['blog_single_leave_comment'] = BlogSingleLeaveComment.objects.all()
#         context['blog_single_tag_cloud'] = BlogSingleTagsCloud.objects.all()
#
#         return context
#
#     def get_object(self):
#         queryset = BlogHomeContent.objects.get(pk=self.kwargs['pk'])
#         return queryset


class PagesView(TemplateView):
    template_name = "portfolio/elements.html"


class ContactView(TemplateView):
    template_name = "portfolio/contact.html"
    model = ContentFormAddressInfo
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['content_form_address'] = ContentFormAddressInfo.objects.all()

        return context


def contactmessage(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]
    send_mal = ContactForm(email=email, name=name, subject=subject, message=message)
    send_mal.save()

    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject=subject, message=message, from_email=from_email,
                  recipient_list=[email], fail_silently=False)
    return HttpResponse({'Your Message is sent Successfully. We will contact you soon. Thank you'})
