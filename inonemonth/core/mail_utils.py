from __future__ import absolute_import

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template


def send_invitation_mail_to_juror(juror, request, juror_registered=False):
    subject = 'Invitation to be a juror of my challenge'
    from_role = juror.challenge.get_clencher()
    from_email = from_role.user.email
    to_email = juror.user.email
    link = request.build_absolute_uri(reverse("juror_challenge_signin", kwargs={"pk": juror.challenge.id}))
    context = {
        'sender': from_email,
        'challenge_title': from_role.challenge.title,
        'link': link,
    }
    if juror_registered:
        text = get_template('email/registered_juror_invitation.txt')
        html = get_template('email/registered_juror_invitation.html')
    else:
        text = get_template('email/new_juror_invitation.txt')
        html = get_template('email/new_juror_invitation.html')
        context["account_email"] = to_email
        context["account_password"] = juror.user.userextension.temp_password

    email_context = Context(context)
    text_content = text.render(email_context)
    html_content = html.render(email_context)

    mail = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    mail.attach_alternative(html_content, "text/html")
    mail.send()
