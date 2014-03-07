from __future__ import absolute_import

from django.template import Library


register = Library()


@register.filter
def get_representation_for_user(role, user_role):
    cap_role_type = role.type.capitalize()
    if user_role.type == "juror":
        if role.type == "clencher":
            return "{0} ({1})".format(cap_role_type, role.user.email)
        elif role.type == "juror":
            if role == user_role:
                return "{0} {1} (me)".format(
                    cap_role_type,
                    role.challenge.get_juror_representation_number(role))
            else:
                return "{0} {1}".format(
                    cap_role_type,
                    role.challenge.get_juror_representation_number(role))
        else:
            raise Exception("Else Die")

    elif user_role.type == "clencher":
        if role.type == "clencher":
            return "{0} (me)".format(cap_role_type)
        elif role.type == "juror":
            return "{0} {1} ({2})".format(
                cap_role_type,
                role.challenge.get_juror_representation_number(role),
                role.user.email)
        else:
            raise Exception("Else Die")

    else:
        raise Exception("Else Die")
