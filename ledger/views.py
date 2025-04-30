from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = ''


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_list')


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipe_update.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = RecipeImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = Recipe.objects.get(pk = self.kwargs['pk'])
            recipe_image.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(** kwargs)
            ctx['form'] = form
            return self.render_to_response(ctx)
