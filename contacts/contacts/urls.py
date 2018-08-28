from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.contacts_app.urls')),

    #url(r'^api/contacts_app/', include("apps.contacts_app.api.urls", namespace='contacts_app-api')),
]
