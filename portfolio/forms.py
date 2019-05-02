from django import forms
from .models import news_subs, ContactForm


class SendMailForm(forms.ModelForm):
    class Meta:
        model = news_subs
        fields = ["news_email"]


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message"]