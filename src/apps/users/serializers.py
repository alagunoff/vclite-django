from rest_framework import serializers

from shared.utils import filter_out_none_values

from .models import User as UserModel


class User(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password', 'first_name', 'last_name',
                  'avatar', 'creation_date', 'is_admin', 'last_login']

    def to_representation(self, instance):
        return filter_out_none_values(super().to_representation(instance))