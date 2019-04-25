from django.urls import path

from .views import IndexView, AutorView

urlpatterns = [
        path('', IndexView.as_view()),
        path('autores/', AutorView.as_view()),

        ]
