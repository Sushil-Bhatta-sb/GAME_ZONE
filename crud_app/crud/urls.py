from django.urls import path
from . import views
urlpatterns = [
   path('',views.register_form,name="register"),
   path('login/',views.login_form,name="login"),
   path('logout/',views.logout_form,name="logout"),
   path('home/',views.home,name="home"),
   path('action/',views.action,name='action'),
   path('sports/',views.sports,name='sports'),
   path('strategy/',views.strategy,name='strategy'),
]
