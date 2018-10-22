from django.urls import include, path
from . import views

urlpatterns = [
    path('track/id/<int:track_id>', views.track),
    path('track/', views.tracks)
]