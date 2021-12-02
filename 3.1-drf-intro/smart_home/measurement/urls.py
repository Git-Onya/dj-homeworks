from django.urls import path
from django.contrib import admin
from measurement.views import SensorView, SensorDetailView, MeasurementView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:sensor>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
