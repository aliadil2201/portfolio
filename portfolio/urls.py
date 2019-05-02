from django.urls import path
import portfolio.views
from django.conf.urls import include, url
from .views import MyView, AboutView, ServicesView, PortfolioView, PriceView, BlogHomeView, PagesView, \
    ContactView,BlogSingleView
    # MyDetailView, BlogSingleView
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', MyView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('price/', PriceView.as_view(), name='price'),
    path('bloghome/', BlogHomeView.as_view(), name='bloghome'),
    path('blogsingle/', BlogSingleView.as_view(), name='blogsingle'),
    # path('bloghome/<int:pk>/', MyDetailView.as_view(), name='detail'),
    path('pages/', PagesView.as_view(), name='pages'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('sendmail/', portfolio.views.sendmail, name='sendmail'),
    path('contactmessage/', portfolio.views.contactmessage, name='contactmessage'),
]
