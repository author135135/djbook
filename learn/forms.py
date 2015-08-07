# -*- encoding: utf-8 -*-
from django import forms
import codecs


class UploadFileForm(forms.Form):
    title = forms.CharField(required=False)
    file = forms.FileField()


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send(self):
        from djbook.settings import MEDIA_ROOT, os

        with codecs.open(os.path.join(MEDIA_ROOT, 'contacts.txt'), 'a+', encoding='utf-8') as f:
            message = u"Name: {name}\r\nMessage: {message}\r\n\r\n".format(**self.cleaned_data)
            f.write(message)

        return True
