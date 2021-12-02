from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from .models import Sensor, Measurement


class SensorView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_url_kwarg = 'sensor'

    def get(self, request, sensor_id):
        sensor = Sensor.objects.get(id=sensor_id)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
