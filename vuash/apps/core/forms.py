from django import forms

from vuash.apps.core.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("data",)
        widgets = {"data": forms.HiddenInput}
