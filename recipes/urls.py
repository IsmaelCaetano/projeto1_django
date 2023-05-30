from django.urls import path

# '.' ferecise a pasta que estou
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
