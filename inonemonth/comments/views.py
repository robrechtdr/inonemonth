from rest_framework import generics
from .models import HeadComment, TailComment
#from .serializers import HeadCommentSerializer, TailCommentSerializer


"""
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
"""
