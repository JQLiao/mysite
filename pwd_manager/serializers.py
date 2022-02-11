from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pwd_manager.models import HostInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostInfo
        fields = ['ip','zone','status','passwd']
