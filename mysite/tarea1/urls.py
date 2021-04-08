from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('temporadas/', views.temporadas, name='temporadas'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('<str:serie>/', views.temporadas, name='temporadas'),
    path('<str:serie>/<int:num_temp>/', views.capitulos, name='capitulos'),
    path('<str:serie>/<int:num_temp>/<int:num_cap>/', views.episodio, name='episodio'),
    path('personajes/<str:p>/', views.personaje, name='personaje'),

]

