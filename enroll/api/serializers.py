from rest_framework import serializers
from enroll.models import databaseintodolist


class todoserializers(serializers.ModelSerializer):
    class Meta:
        model=databaseintodolist
        fields="__all__"