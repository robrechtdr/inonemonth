from rest_framework import serializers
from .models import HeadComment, TailComment




# Currently not necess
"""
class HeadCommentSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve")
    challenge = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = HeadComment
        fields = ("id", "text", "type", "owner", "posted_on",
                  "last_modified_on", "challenge")

"""
class TailCommentSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="role_api_retrieve")
    challenge = serializers.PrimaryKeyRelatedField()
    #head = serializers.HeadCommentSerializer()
    head = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = TailComment
        fields = ("id", "text", "type", "owner", "posted_on",
                  "last_modified_on", "challenge")
