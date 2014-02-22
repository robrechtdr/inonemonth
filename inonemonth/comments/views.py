from __future__ import absolute_import

from rest_framework import generics
from .models import HeadComment, TailComment
from .serializers import TailCommentSerializer #,HeadCommentSerializer

"""
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
"""

class TailCommentDestroyAPIView(generics.DestroyAPIView):
    queryset = TailComment.objects.all()
    serializer_class = TailCommentSerializer

