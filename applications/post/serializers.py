from rest_framework import serializers
from applications.post.models import Post, Comment, Rating, Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Like
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.email")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return Post.objects.create(**validated_data)
        # return super().create(validated_data)

    def to_representation(self, instance):
        # print(instance)
        rep = super().to_representation(instance)
        # print(rep)
        # rep["name"] = "John"
        rep["like_count"] = instance.likes.filter(is_like=True).count()

        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += rating.rating

        if rating_result:
            rep["rating"] = rating_result / instance.ratings.all().count()
        else:
            rep["rating"] = 0

        return rep



class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ("rating",)