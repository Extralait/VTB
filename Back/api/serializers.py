from rest_framework import serializers

from api.models import ProcessingFile


class ProcessingFileSerializer(serializers.ModelSerializer):
    """
    Необработанный файл (сериализатор)
    """
    class Meta:
        model = ProcessingFile
        fields = '__all__'
        read_only_fields = ['id','file_name','file_size','ready_status']
