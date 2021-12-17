"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tours import views as tours_views

handler400 = tours_views.custom_handler400
handler403 = tours_views.custom_handler403
handler404 = tours_views.custom_handler404
handler500 = tours_views.custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', tours_views.TestView.as_view()),
    path('', tours_views.main_view),
    path('departure/<str:departure>', tours_views.departure_view),
    path('tour/<int:id>', tours_views.tour_view),
]
