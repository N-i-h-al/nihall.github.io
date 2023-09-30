from django.urls import path,include
from .router import router
from .views_api import top_sites_api

urlpatterns=[
    path('',include(router.urls)),
    path('api/topsites/', top_sites_api, name='top-sites-api'),
]
