from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from calling_card.views import home, resume


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),
    url(r'^resume/', resume, name='resume'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
