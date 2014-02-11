from django.template import Library

register = Library()

@register.filter
def get_representation_for_user(role, user_role):
    if user_role.type == "juror":
        if role.type == "clencher":
            return "{0} ({1})".format(role.type.capitalize(), role.user.email)
        elif role.type == "juror":
            if role == user_role:
                return "Juror 1 (me)"
            else:
                return "Juror 2"
        else:
            return Exception("Else Die")

    elif user_role.type == "clencher":
        if role.type == "clencher":
            return "Clencher (me)"
        elif role.type == "juror":
            return "Juror 1 (andy.slacker@gmail.com)"
        else:
            return Exception("Else Die")

    else:
        return Exception("Else Die")
