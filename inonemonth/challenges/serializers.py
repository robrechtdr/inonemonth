from rest_framework import serializers

from .models import Challenge, Role
from core.serializers import UserSerializer
#from comments.serializers import HeadCommentSerializer, TailCommentSerializer



class ChallengeSerializer(serializers.ModelSerializer):
    #role_set = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve", many=True)
    #role_set = serializers.RelatedField(many=True)
    #role_set = serializers.SlugRelatedField(many=True, slug_field="type")

    #role_set = RoleSerializer(many=True)
    #get_clencher = serializers.Field(source="get_clencher")
    in_challenge_period = serializers.Field(source="in_challenge_period")

    class Meta:
        model = Challenge
        fields = ("id", "title", "body", "repo_name", "branch_name", "creation_datetime",
                  "headcomment_set", "tailcomment_set",
                  "in_challenge_period")


class RoleSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    #challenge = serializers.RelatedField()
    challenge = ChallengeSerializer()
    #comment_set = CommentSerializer()
    can_make_head_comment = serializers.Field(source="can_make_head_comment")
    is_juror = serializers.Field(source="is_juror")

    class Meta:
        model = Role
        fields = ("id", "user", "type", "challenge",
                  "vote", "can_make_head_comment",
                  "headcomment_set", "tailcomment_set", "is_juror")
                  #"comment_set")
        depth = 2

