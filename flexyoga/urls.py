"""flexyoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import enroll.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('pay', enroll.views.make_payment, name='fee_pay'),
        path('enroll', enroll.views.create, name='enroll_person'),
        path('batch', enroll.views.update_batch, name='update_batch')
    ]))
]
