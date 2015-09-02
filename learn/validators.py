from django.core.exceptions import ValidationError


def homer_validator(value):
    if 'homer' in value.lower():
        raise ValidationError('Please don\'t use Homer name in blog title!', code='invalid')
