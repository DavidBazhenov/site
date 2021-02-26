from django.urls import path
from . import views
urlpatterns=[
    path("",views.advert_list,name='advert_list'),
    path("datascientist",views.datascientist,name='datascientist'),
    path("pythonrazrabotchik",views.pythonrazrabotchik,name='pythonrazrabotchik'),
    path("veb_razrabotchik",views.veb_razrabotchik,name='veb_razrabotchik'),
    path("testirovchik",views.testirovchik,name='testirovchik'),
    path("Java",views.Java,name='Java')
    ]
