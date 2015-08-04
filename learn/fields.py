from django.db import models


class NameInEmailField(models.Field):
    description = "Check is email contains name"

    def __init(self, *args, **kwargs):
        super(NameInEmailField, self).__init__(*args, **kwargs)
