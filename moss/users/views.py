from rest_framework import viewsets
from .serializers import UserSerializer, RoleSerializer, GroupSerializer
from .models import User, Role, Group


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    search_fields = ['username']
    filter_fields = ['groups__name']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_fields = ['name']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ['name']