from djoser.permissions import CurrentUserOrAdmin
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import *
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Стандартная пагинация
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class ProcessingFileViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = ProcessingFileCreateSerializer
    permission_classes = (CurrentUserOrAdmin,)
    filter_fields = [f.name for f in ProcessingFile._meta.fields if not f.__dict__.get('upload_to')]
    ordering_fields = filter_fields

    def get_permissions(self):
        """
        Возвращает права доступа
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Возвращает класс сериализатора
        """
        if self.action == 'list':
            serializer_class = ProcessingFileListSerializer
        elif self.detail:
            serializer_class = ProcessingFileDetailsSerializer
        else:
            serializer_class = ProcessingFileCreateSerializer

        return serializer_class

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = ProcessingFile.objects.all()
        else:
            queryset = ProcessingFile.objects.filter(user=user).all()
        return queryset




