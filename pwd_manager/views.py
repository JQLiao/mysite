from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pwd_manager.models import HostInfo
from pwd_manager.serializers import UserSerializer, GroupSerializer, HostInfoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HostinfoViewSet(viewsets.ModelViewSet):
    queryset = HostInfo.objects.all()
    serializer_class = HostInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def hosts_list(request,  format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = HostInfo.objects.all()
        serializer = HostInfoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HostInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hosts_detail(request, pk,  format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        hostinfo = HostInfo.objects.get(pk=pk)
    except HostInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HostInfoSerializer(hostinfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HostInfoSerializer(hostinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hostinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)