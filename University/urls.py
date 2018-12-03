from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('unimng/', include('unimng.urls')),
    path('admin/', admin.site.urls),
]
