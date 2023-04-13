from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



from IRC_Resurs import settings
from irc_news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('irc_news.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
