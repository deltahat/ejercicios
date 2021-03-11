from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
	class Meta():
		model = File
		fields = ('file', 'timestamp')

'''
class CalculateSerializer(serializers.ModelSerializer):
	class Meta():
		model = Calculate
		fields = ('file_name',
			'file_url',
			'country',
			'total_cost',
			'average_cost',
			'timestamp')
'''