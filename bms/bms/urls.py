
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('events/', include('events.urls')),
    # path('backend/', include('backend.urls')),
]
