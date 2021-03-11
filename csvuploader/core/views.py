from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			context = file_serializer.data
			context['file_url'] = context.pop('file')
			return Response(context, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListFiles(APIView):
	def get(self, request, *args, **kwargs):
		context =  [{files.file.name, files.file.url, files.timestamp} for files in File.objects.all()]
		return Response((context), status=status.HTTP_201_CREATED)