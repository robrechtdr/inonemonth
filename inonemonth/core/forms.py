from __future__ import absolute_import

from django.forms.formsets import BaseFormSet


# The default behavior of formsets sets the initial form as non-required
# http://stackoverflow.com/questions/2406537
# /django-formsets-make-first-required/2422221#2422221
class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
