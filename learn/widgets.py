from django.forms.widgets import Input
from django.utils.html import format_html
from django.forms.utils import flatatt


class LongTextInput(Input):
    input_type = 'text'

    def __init__(self, attrs=None):
        default_attrs = {'size': 100, 'maxlength': 100}
        if attrs:
            default_attrs.update(attrs)
        super(LongTextInput, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)

        return format_html('<input{} />', flatatt(final_attrs))
