from django.urls import path, include
from networkcalapp import views

urlpatterns = [
    path("",views.index, name="index"),
    path("",views.whildcardmask, name="whildcardmask.html"),
    path("",views.subnetquestions, name="subnetquestions.html"),
    path("",views.subnetquestions_rans, name="subnetquestions_rans.html"),
]