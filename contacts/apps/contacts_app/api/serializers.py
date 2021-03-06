from rest_framework.serializers import ModelSerializer

from contacts_app.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]



class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
         
            'title',
            'slug',
            'content',
            'publish',
        ]


