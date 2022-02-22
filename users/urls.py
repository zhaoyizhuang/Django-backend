from django.urls import path

from . import views

# HTTP endpoints
urlpatterns = [
    path('', views.PersonView.as_view()),
    path('<int:uid>', views.PersonDetailView.as_view()),
]