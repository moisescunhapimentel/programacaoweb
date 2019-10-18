from django.urls import path

from .views import homePageView, sobreView, viadoView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sobre', sobreView, name="sobre"),
    path('viado', viadoView, name='viado')
]