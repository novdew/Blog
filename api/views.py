from rest_framework.views import APIView
from .serializers import PostSerializer
from pages.models import Post
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


# Create your views here.
class Home(APIView):
    def get(self, request):
        objs = Post.objects.all()
        result = PostSerializer(objs, many=True)
        return Response(result.data, HTTP_200_OK)


class AllObjects(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class deleteObject(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
