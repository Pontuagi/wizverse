from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def landing(request):
    return render(request, 'landing.html')


class PostListView(LoginRequiredMixin, ListView):
    model = tweet
    template_name = 'home.html'
    context_object_name = 'tweets'
    ordering = ['-datetime']
    # paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    model = tweet
    template_name = 'createPost.html'
    fields = ['text']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)