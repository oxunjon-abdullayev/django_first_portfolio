from django import forms

from app.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ['username','email', 'text']
        # fields = "__all__"
        exclude = ()
