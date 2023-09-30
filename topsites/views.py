from rest_framework import viewsets
from .models import TopSite
from .serializers import TopSiteSerializer

class TopSite_viewset(viewsets.ModelViewSet):
    queryset = TopSite.objects.all()
    serializer_class = TopSiteSerializer
