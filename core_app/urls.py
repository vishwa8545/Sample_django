from django.urls import path

from . import views

app_name = 'core_app'


urlpatterns = [
    path('generate/', views.GETResponseView.as_view(), name='GetResponseView'),
    ]