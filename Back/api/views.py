from djoser.permissions import CurrentUserOrAdmin
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import *


class ProcessingFileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = ProcessingFile.objects.all()
    serializer_class = ProcessingFileCreateSerializer
    permission_classes = (CurrentUserOrAdmin,)

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

    def filter_queryset(self, queryset):
        user = self.request.user
        if user.is_staff:
            pass
        else:
            queryset = queryset.filter(user=user)
        return queryset




