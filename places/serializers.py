from rest_framework import serializers
from .models import Notice, Author


class NoticeSerializer(serializers.Serializer):
    """сериалайзер для правильного отображение данных"""
    title = serializers.CharField(max_length=120)
    address = serializers.CharField(max_length=120)
    description = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        """Создание данных"""
        return Notice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Обновление данных в заметке"""
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance


class NoticeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'address', 'description', 'author_id')