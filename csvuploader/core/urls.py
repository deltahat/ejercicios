from django.urls import path, include
from .views import FileView, ListFiles, NewCalculate

urlpatterns = [
	path('upload', FileView.as_view(), name = 'file-upload'),
	path('csv-history', ListFiles.as_view(), name = 'list-files'),
	path('new-calculate', NewCalculate.as_view(), name = 'new-calculate'),
]