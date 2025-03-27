from rest_framework import serializers
from .models import YouTubeLink


class YouTubeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeLink
        fields = ['id', 'name', 'url', 'description', 'tags']
