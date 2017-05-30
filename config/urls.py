from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from calling_card.views import home, resume

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

    url(r'^$', home, name='home'),
    url(r'^resume/', resume, name='resume'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
