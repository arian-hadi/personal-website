
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('',include('core.urls')),
    path('accounts/', include('accounts.urls'))
]
