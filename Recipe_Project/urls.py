"""
URL configuration for Recipe_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Recipe_app import views
from Recipe_app.views import feedback_view, feedback_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homefun,name='homepage'),
    path('about',views.aboutfun,name="aboutpage"),
    path('Recipe',views.recipefun,name='recipepage'),
    path('Details/<str:pk>/', views.details, name='detailspage'),
    path('signup',views.signup,name='signuppage'),
    path('login',views.loginfun,name='loginpage'),
    path('logout',views.logout,name='logoutpage'),
    path('feedback/', feedback_view, name='feedback_form'),
    path('feedback/success/', feedback_success, name='feedback_success'),
    path('save-recipe/<int:recipe_id>/', views.save_recipe, name='save_recipe'),
    path('saved-list/', views.saved_list, name='saved_list'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)