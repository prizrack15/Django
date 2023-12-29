from django.urls import path

from . import views

urlpatterns = [
    path('<int:days>', views.get_info_about_day_of_week),
    path('<str:days>', views.day_of_week),
    path('', views.Glav_str_week_days),

]