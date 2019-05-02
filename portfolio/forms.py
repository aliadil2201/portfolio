from django import forms
from .models import NewsSubscription, ContactForm


class SendMailForm(forms.ModelForm):
    class Meta:
        model = NewsSubscription
        fields = ["news_email"]


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message"]