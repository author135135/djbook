import re
from django import forms


class PhoneField(forms.CharField):
    description = "Phone number field"
    default_error_messages = {
        'required': 'Please enter your phone number',
        'invalid': 'Enter correct phone number.',
    }

    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(PhoneField, self).to_python(value)
        if not value.strip():
            raise forms.ValidationError('Empty value error', code='invalid')
        return value

    def validate(self, value):
        super(PhoneField, self).validate(value)

        phone_pattern = re.compile('^\+?\s?[0-9]+\(?[0-9]+\)?[0-9-\s]+$')
        if phone_pattern.match(value) is None:
            raise forms.ValidationError(self.error_messages['invalid'], code='invalid')
