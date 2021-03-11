from django.urls import path, include
from .views import FileView, ListFiles

urlpatterns = [
	path('upload/', FileView.as_view(), name = 'file-upload'),
	path('csv-history/', ListFiles.as_view(), name = 'list-files'),
]