import imp
from django.urls import path
from . import views
from django.conf import Settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.newssection , name='news'),
    path('<slug>', views.ide)
    # here slug we are using is defined slug
]
