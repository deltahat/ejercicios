from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File, Calculate

import os
from django.conf import settings
import pandas as pd

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			context = file_serializer.data
			context['file_name']= context['file'].lstrip("/media/")
			context['file_url'] = context.pop('file')
			return Response(context, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListFiles(APIView):
	def get(self, request, *args, **kwargs):
		context =  [{'file_name':files.file.name, 'file_url':files.file.url, 'timestamp':files.timestamp} for files in File.objects.all()]
		return Response((context), status=status.HTTP_201_CREATED)




class NewCalculate(APIView):

	def post(self, request, *args, **kwargs):

		if (('file_name' in request.data) and 
			('country' in request.data)):

			# Obtengo parametros
			file_name = request.data['file_name']
			country = request.data['country']
			file_url = '/media/' + file_name

			# Hago el calculo a partir del cvs 
			total_cost = 1000.30
			average_cost = 10.20

			'''
			# DEBUG
			csv_route = settings.MEDIA_ROOT+"/"+file_name
			print(csv_route)
			data = pd.read_csv(csv_route, names=['country','budget'])
			col_country = list(data.country)
			col_budget = list(data.budget)

			df = pd.DataFrame({'Country':col_country , 'Budget':col_budget})
			df_mask=df['Country']==country
			filtered_df = df[df_mask]
			print(filtered_df)
			'''

			# Registro en base de datos
			calculate = Calculate.objects.create(
				file_name = file_name,
				file_url = file_url,
				country = country,
				total_cost = total_cost,
				average_cost = average_cost
			)
			calculate.save()

			# Armo respuesta
			context = {
				"file_name": calculate.file_name,
				"file_url": calculate.file_url,
				"country": calculate.country,
				"total_cost": calculate.total_cost,
				"average_cost": calculate.average_cost,
				"timestamp": calculate.timestamp
			}

			return Response(context, status=status.HTTP_201_CREATED)
		else:
			return Response({"message": "Error. 'file_name' and 'country' are required."})