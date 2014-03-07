from __future__ import absolute_import

from rest_framework import generics

from .models import TailComment
from .serializers import TailCommentSerializer


class TailCommentDestroyAPIView(generics.DestroyAPIView):
    queryset = TailComment.objects.all()
    serializer_class = TailCommentSerializer
