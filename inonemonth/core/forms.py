import userena.forms


class InonemonthAuthenticationForm(userena.forms.AuthenticationForm):
    """
    Overwrite (__init__()?) to supplement custom "class" and "placeholder" properties to input widgets.
    See : https://github.com/bread-and-pepper/django-userena/blob/master/userena/forms.py

    Also test customized parts of form!!
    """
    pass

    '''
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        #self.fields["identification"] = ...
    '''
