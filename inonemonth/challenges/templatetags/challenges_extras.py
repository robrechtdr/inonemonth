from django.template import Library

register = Library()

@register.filter
def get_representation_for_user(role, user_role):
    cap_role_type = role.type.capitalize()
    juror_representation_number = role.challenge.get_juror_representation_number(role)
    if user_role.type == "juror":
        if role.type == "clencher":
            return "{0} ({1})".format(cap_role_type, role.user.email)
        elif role.type == "juror":
            if role == user_role:
                return "{0} {1} (me)".format(cap_role_type, juror_representation_number)
            else:
                return "{0} {1}".format(cap_role_type, juror_representation_number)
        else:
            return Exception("Else Die")

    elif user_role.type == "clencher":
        if role.type == "clencher":
            return "{0} (me)".format(cap_role_type, juror_representation_number)
        elif role.type == "juror":
            return "{0} {1} ({2})".format(cap_role_type, juror_representation_number, role.user.email)
        else:
            return Exception("Else Die")

    else:
        return Exception("Else Die")