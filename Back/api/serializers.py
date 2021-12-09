from rest_framework import serializers

from api.models import ProcessingFile
from api.services.vtb_handler.main import file_checker


class ProcessingFileSerializer(serializers.ModelSerializer):
    """
    Необработанный файл (сериализатор)
    """
    class Meta:
        model = ProcessingFile
        fields = '__all__'
        read_only_fields = ['id','file_name','file_size','ready_status',
                            'result_json','created_at','user']

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
        result_json = file_checker(file_path)
        print(result_json)
        processing_file.result_json = result_json
        processing_file.ready_status = True
        processing_file.save()
        return processing_file

