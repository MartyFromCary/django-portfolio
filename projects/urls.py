from django.urls import path
from projects import views

#app_name = 'projects' #?

urlpatterns = [
    path('', views.project_list),
]