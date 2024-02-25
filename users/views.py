from django.shortcuts import render, get_object_or_404, redirect
from .models import tweet
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse

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
    

@login_required
def agree_post(request, post_id):
    post = get_object_or_404(tweet, pk=post_id)
    post.agreements += 1
    post.save()
    return JsonResponse({'agree_count': post.agreements, 'disagree_count': post.disagreements})

@login_required
def disagree_post(request, post_id):
    post = get_object_or_404(tweet, pk=post_id)
    post.disagreements += 1
    post.save()
    return JsonResponse({'agree_count': post.agreements, 'disagree_count': post.disagreements})