from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import SlotSerializer, ValueConstraintSerializer
from utterance.services.slot_validation_services import ValidateSlotValues
from utterance.services.value_constraint_services import ValidateNumericConstraint


# Create your views here.

def index(request):
    return HttpResponse('Utterance API')


class ValidateSlotView(APIView):

    def post(self, request, format=None):
        
        serializer = SlotSerializer(data=request.data)
        if serializer.is_valid():
            obj = ValidateSlotValues(serializer.data)
            return_response = obj.get_validation_results()
            return Response(return_response , status=status.HTTP_200_OK)
        
        return Response({}, status=status.HTTP_200_OK)


class ValidateNumericConstraintView(APIView):

    def post(self, request, format=None):

        serializer = ValueConstraintSerializer(data=request.data)
        if serializer.is_valid():
            obj = ValidateNumericConstraint(serializer.data)
            return_response = obj.get_validation_results()
            return Response(return_response , status=status.HTTP_200_OK)
        
        return Response({serializer.errors}, status=status.HTTP_200_OK)


