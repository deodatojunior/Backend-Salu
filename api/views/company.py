from rest_framework import viewsets
from api.models.company.models import Company
from api.serializers.company import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
