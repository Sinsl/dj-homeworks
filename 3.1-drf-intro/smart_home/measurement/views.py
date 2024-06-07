# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        data = request.data
        Sensor.objects.create(name=data.get('name'), description=data.get('description'))
        return Response(data=data)


class SensorRetrieveView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def PATCH(self, request, pk):
        data = request.data
        description = data.get('description')
        sensor = Sensor.objects.filter(id=pk).update(description=description)
        return Response(data=sensor)


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = request.data
        Measurement.objects.create(sensor_id=data.get('sensor'), temperature=data.get('temperature'))
        return Response(data=data)
