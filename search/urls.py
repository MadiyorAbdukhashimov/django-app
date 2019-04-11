from django.urls import path
#
from .views import (
    SearchProductList,
)
#

urlpatterns = [
    path(r'', SearchProductList.as_view(), name='query'),
]
