from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'EstateNg Admin'
admin.site.site_title = 'EstateNg Admin Portal'
admin.site.index_title = 'Welcome to the EstateNg Portal'
