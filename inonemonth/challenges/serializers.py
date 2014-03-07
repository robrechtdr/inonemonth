from __future__ import absolute_import

from rest_framework import serializers

from .models import Challenge, Role


class ChallengeSerializer(serializers.ModelSerializer):
    in_challenge_period = serializers.Field(source="in_challenge_period")
    has_ended = serializers.Field(source="has_ended")

    class Meta:
        model = Challenge
        fields = ("id", "title", "body", "repo_name", "branch_name",
                  "creation_datetime", "headcomment_set", "tailcomment_set",
                  "in_challenge_period", "has_ended")


class RoleSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer()
    can_make_head_comment = serializers.Field(source="can_make_head_comment")
    is_juror = serializers.Field(source="is_juror")

    class Meta:
        model = Role
        fields = ("id", "user", "type", "challenge",
                  "vote", "can_make_head_comment",
                  "headcomment_set", "tailcomment_set", "is_juror")
        depth = 2
