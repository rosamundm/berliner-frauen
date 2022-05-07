from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import District, Street
from .serializers import DistrictSerializer, StreetSerializer


# for "/"
def index(request):
    return render(request, "streets/index.html")


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer
    lookup_field = "district_slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all().order_by("name")
    serializer_class = StreetSerializer
    lookup_field = "street_slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None