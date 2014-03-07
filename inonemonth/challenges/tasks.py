from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from core.allauth_utils import create_allauth_user, generate_password
from core.mail_utils import send_invitation_mail_to_juror
from core.models import UserExtension

from inonemonth.celery import app
from .models import Role

User = get_user_model()


# Celery tasks can't accept a request object
@app.task
def invite_juror(email, challenge, url_base):
    # Email address of juror is of already registered user
    try:
        user = User.objects.get(email=email)
        juror = Role.objects.create(user=user, challenge=challenge,
                                    type=Role.JUROR)
        send_invitation_mail_to_juror(juror=juror,
                                      url_base=url_base,
                                      juror_registered=True)

    # Email address of juror is of not already registered user
    except ObjectDoesNotExist:
        password = generate_password()
        user = create_allauth_user(email=email,
                                   password=password)
        # Hashed passwords can't be retrieved, so they'll need to be
        # stored somewhere to send that temporary password to the user.
        # The user can then change the password himself later on.
        UserExtension.objects.create(user=user, temp_password=password)

        juror = Role.objects.create(user=user, challenge=challenge,
                                    type=Role.JUROR)
        send_invitation_mail_to_juror(juror=juror,
                                      url_base=url_base,
                                      juror_registered=False)
