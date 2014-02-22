from __future__ import absolute_import

import random
import string

from django.conf import settings
from django.http import HttpRequest, QueryDict
from django.utils.importlib import import_module

from allauth.account import app_settings, signals
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from allauth.account.utils import setup_user_email, complete_signup


# http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
def generate_password(chars=8):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(chars))


def get_post_dic(email, password):
    #csrfmiddlewaretoken = #not necessary
    return {
            u'password1': password,
            #u'csrfmiddlewaretoken': #not necessary
            u'email': email,
            u'password2': password,
            u'confirmation_key': ""
    }


def get_signin_request(post_dic):
    signin_request = HttpRequest()

    query_dict = QueryDict("")
    query_dict_post = query_dict.copy() # Make it mutable
    query_dict_get = query_dict.copy() # Make it mutable

    query_dict_post.update(post_dic)

    signin_request.POST = query_dict_post
    signin_request.GET = query_dict_get

    # Set session (fails without)
    # http://stackoverflow.com/questions/16865947/django-httprequest-object-has-no-attribute-session
    engine = import_module(settings.SESSION_ENGINE)
    session_key = None
    signin_request.session = engine.SessionStore(session_key)

    signin_request.SERVER_NAME = ""

    return signin_request


def create_allauth_user(email, password):
    post_dic = get_post_dic(email, password)
    signin_request = get_signin_request(post_dic)

    signup_form_kwargs = {"files": {}, "initial": {},
                          "data": signin_request.POST}
    # From allauth.account.views.SignupView.form_valid
    signup_form = SignupForm(**signup_form_kwargs)
    signup_form.cleaned_data = post_dic # Csrf token not neccesary either
    user = signup_form.save(signin_request)

    # Sends sign up mail, alter to invite mail later on
    signals.user_signed_up.send(sender=user.__class__,
                                request=signin_request,
                                user=user,
                                signal_kwargs={})

    return user
