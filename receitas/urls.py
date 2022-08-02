from django.urls import path
from receitas.views import contato, home, sobre


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),

]