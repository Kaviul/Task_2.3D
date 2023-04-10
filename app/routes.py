from . import views
from django.urls import path

# URLConfig
urlpatterns = [
    # path('1/', views.user),
    # path('db/', views.db),


    path('', views.my_form, name='save_form_data'),


]
