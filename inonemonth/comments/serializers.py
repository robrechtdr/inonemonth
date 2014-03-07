from __future__ import absolute_import

from rest_framework import serializers

from .models import TailComment


class TailCommentSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve")
    challenge = serializers.PrimaryKeyRelatedField()
    head = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = TailComment
        fields = ("id", "text", "type", "owner", "posted_on",
                  "last_modified_on", "challenge")
