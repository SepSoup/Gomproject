from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("foundRegistery", views.foundreg, name="foundreg"),
    path("found", views.found, name="found"),
    path("lostRegistery", views.lostreg, name="lostreg"),
    path("lost", views.lost, name="lost"),
    path("info/<int:obj_id>", views.info, name="info")
]