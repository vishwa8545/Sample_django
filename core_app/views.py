from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status


class GETResponseView(APIView):

    """
    API view for the clas

    """

    def get(self,request):
        return JsonResponse({"message": " Successfully  Request Sent to Model", "status": "Success"},
                                    status=status.HTTP_200_OK, safe=False)


