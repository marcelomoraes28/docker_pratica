from rest_framework import mixins, viewsets
from rest_framework.response import Response

from register.api.serializer import RegisterSerializer
from register.tasks import register
from register.models import Register as reg


class RegisterViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    This endpoint register
    """
    queryset = reg.objects.all()
    serializer_class = RegisterSerializer

    def list(self, request, *args, **kwargs):
        return Response({'qtd': reg.objects.all().count()})

    def create(self, request, *args, **kwargs):
        register.delay()
        return Response({'message': 'Register Created'})
