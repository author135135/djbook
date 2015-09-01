# -*- encoding: utf-8 -*-
from django import forms
from django.forms.utils import ErrorList
from django.utils.formats import mark_safe
import codecs


class UploadFileForm(forms.Form):
    title = forms.CharField()
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


class TestForm(forms.Form):
    login = forms.CharField(max_length=70)
    password = forms.CharField(widget=forms.PasswordInput)


class NameForm(TestForm):
    from learn.fields import PhoneField
    from learn.widgets import LongTextInput

    required_css_class = 'form-required-field'
    your_name = forms.CharField(max_length=100, initial='Initial value')
    phone = PhoneField(label='Your Phone', widget=LongTextInput)


# Custom errors class
class DivErrorList(ErrorList):
    def __unicode__(self):
        if not self:
            return ''
        else:
            return mark_safe(u'<div class="error">{0}</div>'.format("\n".join([u'<p>{0}</p>'.format(e) for e in self])))
