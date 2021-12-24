from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)
    #
    # def validate(self, data):
    #     """Метод для валидации. Вызывается при создании и обновлении."""
    #
    #     # TODO: добавьте требуемую валидацию
    #     # creator = data.get('user')
    #     # opened_ads = len(Advertisement.objects.filter(creator=creator, status='OPEN'))
    #     # if opened_ads >= 10:
    #     #     raise ValidationError('You can keep opened only 10 ads')
    #     return data
