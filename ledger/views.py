from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe
from .forms import RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    form_class = RecipeForm


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe_detail.html'
    form_class = RecipeForm
