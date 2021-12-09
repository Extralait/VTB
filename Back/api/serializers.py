from rest_framework import serializers

from api.models import ProcessingFile
from api.services.vtb_handler.main import file_checker


class ProcessingFileCreateSerializer(serializers.ModelSerializer):
    """
    Необработанный файл (сериализатор)
    """

    class Meta:
        model = ProcessingFile
        fields = ['id', 'file_object', 'file_name', 'total_archives','result_file_object',
                  'ready_status', 'created_at', 'total_danger', 'total_files','result_file_size' ]

        read_only_fields = ['id', 'file_name', 'total_archives','result_file_object',
                            'ready_status', 'created_at', 'total_danger', 'total_files','result_file_size' ]

    def _user(self):
        """
        Получение текущего пользователя
        """
        return self.context['request'].user

    def create(self, validated_data):
        """
        Создать файл
        """
        processing_file = (ProcessingFile.objects.create(
            user=self._user(),
            **validated_data
        ))

        file_path = processing_file.file_object.path
        result_json, output_path = file_checker(file_path)
        processing_file.result_json = result_json
        processing_file.result_file_object = output_path
        processing_file.ready_status = True
        processing_file.total_danger = result_json['xml_data']['malicious_objects']
        processing_file.total_files = result_json['xml_data']['total_objects']
        processing_file.total_archives = result_json['xml_data']['total_archives']
        processing_file.result_file_size = result_json['xml_data']['output_xml_size']
        processing_file.save()
        return processing_file


class ProcessingFileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessingFile
        fields = ['id', 'file_object', 'file_name', 'result_file_size', 'total_archives',
                  'ready_status', 'created_at', 'total_danger', 'total_files', 'result_file_object' ]


class ProcessingFileDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessingFile
        fields = '__all__'

