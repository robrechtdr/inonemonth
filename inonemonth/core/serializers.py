from django.contrib.auth import get_user_model
from rest_framework import serializers
#from challenges.serializers import RoleSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    #role_set = serializers.PrimaryKeyRelatedField(many=True)
    #role_set = RoleSerializer()
    role_set = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve", many=True)
    socialaccount_set = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", "role_set", "socialaccount_set")
