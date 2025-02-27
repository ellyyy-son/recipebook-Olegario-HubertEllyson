from django.urls import path
from .views import index, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='list'),
]

app_name = "ledger"