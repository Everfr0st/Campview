from django.urls import path

from . import views

urlpatterns = [
    # Página de índice "/polls/"
    path('', views.index, name='index'),
    #select view
    path('select/', views.select, name='select'),
    #village view
    path('village/', views.villages, name='village'),
    #cabain view
    path('cabains/<int:idvil>/', views.visucabagna, name='cabain'),
    #camper view
    path('campers/<int:idvil>/<int:idcab>', views.visucampista, name='camper'),
    #camper profile
    path('campista/<int:idvil>/<int:idcab>/<int:idcamper>', views.visu_profile_camper, name='profile'),
    #login view
    path('logout/', exit, name='exit'),

]