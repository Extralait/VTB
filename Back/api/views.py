from djoser.permissions import CurrentUserOrAdmin
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *


class ProcessingFileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = ProcessingFile.objects.all()
    serializer_class = ProcessingFileSerializer
    permission_classes = (CurrentUserOrAdmin,)



