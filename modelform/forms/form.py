from django import forms

from .models import ContactForm


class Contact(forms.ModelForm):
    class Meta:
        model=ContactForm
        fields=['name','phone']

        def clean_phone(self):
            phone=self.cleaned_data.get('phone')
            if str(phone).length<11:
                raise forms.ValidationError("phone number to short")