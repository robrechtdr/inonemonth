from rest_framework import serializers
from .models import Challenge, Role

from core.serializers import UserSerializer
from comments.serializers import CommentSerializer


class RoleSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    #challenge = serializers.RelatedField()
    #comment_set = CommentSerializer()

    class Meta:
        model = Role
        fields = ("id", "user", "type", "challenge", "comment_set")
        depth = 2


class ChallengeSerializer(serializers.ModelSerializer):
    #role_set = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve", many=True)
    #role_set = serializers.RelatedField(many=True)
    #role_set = serializers.SlugRelatedField(many=True, slug_field="type")
    role_set = RoleSerializer(many=True)

    class Meta:
        model = Challenge
        fields = ("id", "title", "body", "repo_name", "creation_datetime",
                  "role_set")
