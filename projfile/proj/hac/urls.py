from django.urls import path 
from.import views 

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),  # Update the URL pattern for login
    path('blog/', views.blog, name='blog'),
    path('merchandise/', views.merchandise, name='merchandise'),
    path('ecospace/', views.ecospace, name='ecospace'),
]