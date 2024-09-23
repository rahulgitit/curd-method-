
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Rahul Admin"
admin.site.site_title = "Rahul Admin Portal"
admin.site.index_title = "Welcome to Rahul Researcher Portal"
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.index, name="index"),
    path("delete/<int:id>/", views.delete,name="delete"), # type: ignore
    path("edit/<int:id>/", views.edit,name="edit"),
    path("api/", include('enroll.api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
