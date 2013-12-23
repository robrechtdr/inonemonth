from django.db.models import Model


def get_parent_model_fields_only(model):
    """
    Get only the fields defined in parent models


    class Profile(UserenaBaseProfile):
        user = models.OneToOneField(get_user_model(), unique=True,
                                    verbose_name=_('user'))

    > Profile._meta.get_all_field_names()
    ['challenge_set_judges', 'challenge_set_lincoln', u'id', 'mugshot', 'privacy', 'user']

    Compare with

    > get_parent_model_fields_only(Profile)
    ['mugshot', 'privacy']
    """
    parent_field_names = []
    for model_in_mro in model.__mro__:
        # Stop when base Model is reached
        if model_in_mro == Model:
            break
        # Get field names defined in parents
        if model_in_mro != model:
            parent_field_names = parent_field_names + model_in_mro._meta.get_all_field_names()

    return parent_field_names


def get_reverse_relational_field_names(model):
    """
    Collect relational field names pointing to model from other models.

    > get_reverse_relational_field_names(Profile)
    ["challenge_set_lincoln", "challenge_set_judges"]
    """
    reverse_field_names = []
    for related_field in model._meta.get_all_related_objects():
        reverse_field_names.append(related_field.field.related_query_name())
    for m2m_field in model._meta.get_all_related_many_to_many_objects():
        reverse_field_names.append(m2m_field.field.related_query_name())
    return reverse_field_names

def get_non_reverse_relational_field_names(model):
    """
    Get all non-reverse relation field names.

    > Profile._meta.get_all_field_names()
    ['challenge_set_judges', 'challenge_set_lincoln', u'id', 'mugshot', 'privacy', 'user']

    Compare with

    > get_non_reverse_relational_field_names(Profile)
    [u'id', 'mugshot', 'privacy', 'user']

    """
    all_field_names = model._meta.get_all_field_names()
    reverse_field_names = get_reverse_relational_field_names(model)
    difference = set(all_field_names).difference(set(reverse_field_names))
    return list(difference)


def get_only_fields_defined_in_child_model(model):
    """
    Get only the fields defined in the child model.

    class Profile(UserenaBaseProfile):
        user = models.OneToOneField(get_user_model(), unique=True,
                                    verbose_name=_('user'))

    > Profile._meta.get_all_field_names()
    ['challenge_set_judges', 'challenge_set_lincoln', u'id', 'mugshot', 'privacy', 'user']

    Compare with

    > get_non_reverse_relational_field_names(Profile)
    [u'id', 'user']
    """
    non_reverse_relational_fields = set(get_non_reverse_relational_field_names(model))
    parent_model_fields_only = set(get_parent_model_fields_only(model))
    return list(non_reverse_relational_fields.difference(parent_model_fields_only))
