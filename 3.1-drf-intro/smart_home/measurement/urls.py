from django.urls import path
from .views import SensorView, SensorRetrieveView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensor/<pk>/', SensorRetrieveView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
