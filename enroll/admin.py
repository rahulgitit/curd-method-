from django.contrib import admin
from enroll.models import databaseintodolist
# Register your models here.

@admin.register(databaseintodolist)
class databasetodolistAdmin(admin.ModelAdmin):
    list_display=["id","title","descriptions"]