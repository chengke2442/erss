from django.urls import path

from . import views


urlpatterns = [
    # ex: /users/1,2
    path('<int:request_id>/', views.rideDetail, name='rideDetail'),
]
