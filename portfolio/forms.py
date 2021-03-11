from django.forms import ModelForm
from .models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
