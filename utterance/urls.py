from django.urls import path, include
from utterance import views 

urlpatterns = [
     path('', views.index, name='index'),
     path('validate-slot', views.ValidateSlotView.as_view(), name = 'validate-slot'),
     path('validate-number-constraint', views.ValidateNumericConstraintView.as_view(), 
     name = 'validate-number-constraint')
]