from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'', include('core.urls', namespace='core')),
    url(r'^food/', include('food.urls', namespace='food')),
]
