from rest_framework.viewsets import ModelViewSet
from enroll.models import databaseintodolist
from enroll.api.serializers import todoserializers 
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class todolistapi(ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = databaseintodolist.objects.all()
    serializer_class=todoserializers
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['title']

    # filter_backends=[SearchFilter]
    # search_fields=['title']


   
    filter_backends=[SearchFilter]
    # search_fields=['title','passby ']
    search_fields=['^title']
    # filter_backends=[OrderingFilter]
    