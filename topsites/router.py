from rest_framework import routers
from .views import TopSite_viewset

router = routers.DefaultRouter()
router.register('TopSite',TopSite_viewset)