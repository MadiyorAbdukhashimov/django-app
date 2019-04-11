from django.urls import path
#
from .views import (
    ProductList,
    # ProductDetailView,
    ProductDetailSlugView
    )
#

from django.conf.urls import url

urlpatterns = [
    path(r'', ProductList.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
