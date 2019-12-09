from rest_framework import serializers

from tal_capital.core.models import Post
from tal_capital.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'user',)

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation
