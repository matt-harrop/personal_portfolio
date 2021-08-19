from django.forms import ModelForm
from .models import Message
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email_address', 'content']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email',
            'content': 'Your Message'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                    'class': 'form-control col-sm-6'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                    'class': 'form-control col-sm-6'
                }
            ),
            'email_address': forms.EmailInput(
                attrs={
                    'placeholder': 'Email Address',
                    'class': 'form-control'
                }
            ),
            'sender_phone': forms.TextInput(
                attrs={
                    'placeholder': 'Phone Number',
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Let me know whatever is in your heart...',
                    'class': 'form-control',
                    'style': 'border: none',
                    'rows': 4
                }
            )
        }