from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# https://stackoverflow.com/questions/68968059/how-can-i-allow-users-to-create-their-own-posts-in-django
def create_post(request):
    queryset = Post.content
    template_name = "post_form.html"
    Postform = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Post(
                content=post_form.cleaned_data["content"],
            )
            post.save()

    context = {
        "create_post":create_post,
    }

    return render(request, "post_form.html",)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"

def post_detail(request, slug):
    """
    Display an individual :model:`feed.Post`.

    **Context**

    ``post``
        An instance of :model:`feed.Post`.

    **Template:**

    :template:`feed/post_detail.html`
    """
    if request.method == "POST":
        print("Received a POST request")
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.all().count() 
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
            'Comment submitted and awaiting approval')

    comment_form = CommentForm()
    print("About to render template")
    return render(
        request,
        "feed/post_detail.html",
        { "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
