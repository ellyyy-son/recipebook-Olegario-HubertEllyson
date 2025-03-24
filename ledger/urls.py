from django.urls import path, include
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView


urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='task-create'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='task-update'),
]

app_name = "ledger"
