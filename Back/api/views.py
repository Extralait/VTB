from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import *


class ProcessingFileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = ProcessingFile.objects.all()
    serializer_class = ProcessingFileSerializer


