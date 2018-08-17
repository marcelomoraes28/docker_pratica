from rest_framework import serializers
from register.models import Register as reg


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = reg
        fields = ('id',)

