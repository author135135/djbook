import re
from django.forms import forms


class PhoneField(forms.Field):
    description = "Phone number field"
    default_error_messages = {
        'required': 'Please enter your phone number',
        'invalid': 'Enter correct phone number.',
    }

    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(*args, **kwargs)

    def validate(self, value):
        super(PhoneField, self).validate(value)

        phone_pattern = re.compile('^\+?\s?[0-9]+\(?[0-9]+\)?[0-9-\s]+$')
        if phone_pattern.match(value) is None:
            raise forms.ValidationError(self.error_messages['invalid'], code='invalid')
        return value
