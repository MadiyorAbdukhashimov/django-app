from django.contrib import admin
from django.urls import path
from .views import home_page, contact_page, about_page, login_page, register_page
#
from django.conf import settings
from django.conf.urls.static import static
#

from django.conf.urls import url, include

urlpatterns = [
    url('contact/', contact_page, name='contact'),
    url('login/', login_page, name='login'),
    url('register/', register_page, name='register'),
    url('home/', home_page, name='home'),
    url('about/', about_page, name='about'),
    path('admin/', admin.site.urls),

    url('products/', include(('products.urls','products'), namespace='products')),
    url('search/', include(('search.urls','search'), namespace='search')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
