from django.contrib import admin
from django.urls import path, include

from django_member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_member/', include('django_member.urls'))
]
