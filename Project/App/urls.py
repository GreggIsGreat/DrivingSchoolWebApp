from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Register/',views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('LogOut/', views.LogOut, name='LogOut'),
    path('Admin/', views.Admin, name='Admin'),
]
urlpatterns += staticfiles_urlpatterns()