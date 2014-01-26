from rest_framework import serializers
from .models import Challenge, Role

from core.serializers import UserSerializer


class RoleSerializer(serializers.ModelSerializer):
    #user = serializers.RelatedField(many=True)
    #user = serializers.PrimaryKeyRelatedField()
    #user = serializers.HyperlinkedRelatedField()
    user = UserSerializer()
    #challenge = ChallengeSerializer()
    challenge = serializers.RelatedField()

    class Meta:
        model = Role
        fields = ("id", "user", "type", "challenge")


class ChallengeSerializer(serializers.ModelSerializer):
    #role_set = serializers.HyperlinkedRelatedField(view_name="role_api_detail", many=True)
    #role_set = serializers.RelatedField(many=True)
    #role_set = serializers.SlugRelatedField(many=True, slug_field="type")
    role_set = RoleSerializer(many=True)

    class Meta:
        model = Challenge
        fields = ("id", "title", "body", "repo_name", "creation_datetime",
                  "role_set")
