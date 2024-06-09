from django.urls import path
from .views import SensorView, SensorUpdateView, SensorRetrieveView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensor/update/<pk>', SensorUpdateView.as_view()),
    path('sensor/<pk>/', SensorRetrieveView.as_view()),
    path('measurement', MeasurementView.as_view())
]
