from django.urls import path, include
from utterance import views 

urlpatterns = [
     path('', views.index ),
]