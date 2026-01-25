from django.urls import path
from . import views
urlpatterns = [
   path('<str:name>/',views.home,name='home'),
   path('index/',views.index,name='index'),
   path('',views.add,name='add'),
]
