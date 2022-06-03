from rest_framework import viewsets
from api.models.company.models import Company
from api.serializers.company import *


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
