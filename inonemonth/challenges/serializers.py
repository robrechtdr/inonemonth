from rest_framework import serializers

from .models import Challenge, Role
from core.serializers import UserSerializer
#from comments.serializers import HeadCommentSerializer, TailCommentSerializer


class RoleSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    #challenge = serializers.RelatedField()
    #comment_set = CommentSerializer()
    can_make_head_comment = serializers.Field(source="can_make_head_comment")
    can_vote = serializers.Field(source="can_vote")

    class Meta:
        model = Role
        fields = ("id", "user", "type", "challenge",
                  "vote", "can_vote", "can_make_head_comment")
        depth = 2


class ChallengeSerializer(serializers.ModelSerializer):
    #role_set = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve", many=True)
    #role_set = serializers.RelatedField(many=True)
    #role_set = serializers.SlugRelatedField(many=True, slug_field="type")
    role_set = RoleSerializer(many=True)
    get_clencher = serializers.Field(source="get_clencher")

    class Meta:
        model = Challenge
        fields = ("id", "title", "body", "repo_name", "creation_datetime",
                  "role_set", "get_clencher", "headcomment_set", "tailcomment_set")
