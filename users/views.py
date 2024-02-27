from django.shortcuts import render, get_object_or_404, redirect
from .models import tweet
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse

def landing(request):
    return render(request, 'landing.html')


def handle_agreement(request, post_id, model_field):
    post = get_object_or_404(tweet, pk=post_id)
    user = request.user
    agreement, created = model_field.through.objects.get_or_create(tweet_id=post_id, user=user)
    if not created:
        agreement.delete()
    else:
        other_field = post.disagreements if model_field == post.agreements else post.agreements
        other_field.remove(user)
    post.save()
    return JsonResponse({'agree_count': post.agreements.count(), 'disagree_count': post.disagreements.count()})


@login_required
def agree_post(request, post_id):
    return handle_agreement(request, post_id, tweet.agreements)


@login_required
def disagree_post(request, post_id):
    return handle_agreement(request, post_id, tweet.disagreements)


class PostListView(LoginRequiredMixin, ListView):
    # Class render view to post a Post
    model = tweet
    template_name = 'home.html'
    context_object_name = 'tweets'
    ordering = ['-datetime']
    # paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    # Class to render view to create Post
    model = tweet
    template_name = 'createPost.html'
    fields = ['text']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

