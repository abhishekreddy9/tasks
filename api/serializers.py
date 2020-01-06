from rest_framework import serializers
from .models import TaskGroup, Task, User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = ('title', 'user')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('content', 'tasks')
