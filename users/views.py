from django.shortcuts import render, get_object_or_404, redirect
from .models import tweet, Comment
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


def post_detail(request, tweet_id):
    post = get_object_or_404(tweet, pk=tweet_id)
    return render(request, 'post_view.html', {'tweet': post})


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
    

class AddCommentView(LoginRequiredMixin,View):
    def post(self, request, tweet_id):
        # Retrieve the tweet object based on the tweet_id
        try:
            post = tweet.objects.get(pk=tweet_id)
        except tweet.DoesNotExist:
            messages.error(request, 'Tweet does not exist')
            return redirect('home') 
        
        # Create a new comment object using the data submitted in the form
        comment_text = request.POST.get('text')
        comment = Comment.objects.create(tweet=post, text=comment_text)
        
        return redirect('post_detail', tweet_id=tweet_id)

    def get(self, request, tweet_id):
        post = get_object_or_404(tweet, pk=tweet_id)
        return render(request, 'add_comment.html', {'tweet': post})

