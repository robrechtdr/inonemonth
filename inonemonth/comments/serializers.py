from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve")

    class Meta:
        model = Comment
        fields = ("id", "text", "type", "owner", "posted_on",
                  "last_modified_on")
