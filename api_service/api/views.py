import requests
from django.http import Http404
from requests import RequestException
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.api_utils import get_data_points, get_data_points_for_name, is_datapoint_name_in_db, is_request_data_valid
from api.serializers import DataPointSerializer


class DataPointList(APIView):
    def get(self, request):
        from_timestamp = request.GET.get('from')
        to_timestamp = request.GET.get('to')
        data_points = get_data_points(from_timestamp, to_timestamp)
        serializer = DataPointSerializer(data_points, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataPointSerializer(data=request.data, many=True)
        # TODO Validate each entry separately
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataPointQuery(APIView):
    def get(self, request, datapoint_name):
        if not is_datapoint_name_in_db(datapoint_name):
            raise Http404
        from_timestamp = request.GET.get('from')
        to_timestamp = request.GET.get('to')

        if not is_request_data_valid(from_timestamp, to_timestamp):
            return Response('Invalid timestamp type', status=status.HTTP_400_BAD_REQUEST)

        data_points = get_data_points_for_name(datapoint_name, from_timestamp, to_timestamp)
        values = data_points.values_list('v')

        if not values:
            return Response('No values for this time range', status=status.HTTP_400_BAD_REQUEST)
        payload_dict = {'values': values}

        try:
            calculation_api_response = requests.post('http://calculation-service:8800/api/aggregate-data/',
                                                     data=payload_dict)
        except RequestException:
            return Response('Failed to connect to Calculation API', status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            if calculation_api_response.status_code != 200:
                return Response(status=calculation_api_response.status_code)
        return Response(calculation_api_response.json())


class ApiStatusView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
