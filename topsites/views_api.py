from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import TopSite
from .serializers import TopSiteSerializer

@api_view(['GET'])
def top_sites_api(request):
    if request.method == 'GET':
        top_sites = TopSite.objects.all()
        serializer = TopSiteSerializer(top_sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
