from __future__ import absolute_import

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from core.mail_utils import send_invitation_mail_to_juror
from core.allauth_utils import create_allauth_user, generate_password
from core.models import UserExtension

from .models import Role


User = get_user_model()


# Celery tasks can't accept a request object
@shared_task
def invite_juror(email, challenge, url_base):
    # Email juror is of already registered user
    try:
        user = User.objects.get(email=email)
        juror = Role.objects.create(user=user, challenge=challenge,
                                    type=Role.JUROR)
        send_invitation_mail_to_juror(juror=juror,
                                        url_base=url_base,
                                        juror_registered=True)

    # Email is not of already registered user
    except ObjectDoesNotExist:
        password = generate_password()
        user = create_allauth_user(email=email,
                                    password=password)
        # hashed passwords can't be retrieved, so they'll need to be
        # stored somewhere to send that temporary password to the user.
        # The user can then change the password by himself later on.
        UserExtension.objects.create(user=user, temp_password=password)

        juror = Role.objects.create(user=user, challenge=challenge,
                                    type=Role.JUROR)
        send_invitation_mail_to_juror(juror=juror,
                                        url_base=url_base,
                                        juror_registered=False)
