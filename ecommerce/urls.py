from django.contrib import admin
from django.urls import path
from .views import home_page, contact_page, about_page, login_page, register_page
#
from products.views import ProductList, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static
#

from django.conf.urls import url

urlpatterns = [
    url('contact/', contact_page),
    url('login/', login_page),
    url('register/', register_page),
    url('home/', home_page),
    url('about/', about_page),
    path('admin/', admin.site.urls),

    path('products/', ProductList.as_view()),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
