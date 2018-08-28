from rest_framework.generics import (
    CreateApIView,
    CreateDestroyView,
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    
    )

from contacts_app.models import Post

from .serializers import (
    PostCreateSerializer,
    PostDetailSerializer,
    PostListSerializer
    )


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    #lookup_field = 'slug'



class PostDetailAPIView(RetriveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(RetriveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'    

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    #def get_queryset()