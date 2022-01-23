from rest_framework.response import Response
from rest_framework.views import APIView

DATAPOINT_API_URL = 'http://127.0.0.1:8000/api/'


class CalculationView(APIView):
    def post(self, request):
        values = request.data.getlist('values')
        value_sum = round(sum([float(value) for value in values]), 2)
        value_mean = round(value_sum / len(values), 2)

        response_values = {'avg': value_mean, 'sum': value_sum}
        return Response(response_values)

