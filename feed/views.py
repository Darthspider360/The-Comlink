from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from cloudinary.models import CloudinaryField

# https://stackoverflow.com/questions/68968059/how-can-i-allow-users-to-create-their-own-posts-in-django


def create_post(request):
    if request.method == "POST":
        Post_form = PostForm(request.POST, request.FILES)
        if Post_form.is_valid():
            content = Post_form.save(commit=False)
            content.author = request.user
            content.save()
            messages.add_message(request, messages.SUCCESS, 'posted')
        return HttpResponseRedirect(reverse("home"))
        # redirecting to a new URL
    Post_form = PostForm()
    return render(request, "feed/post_form.html", {"Post_form": Post_form})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "feed/index.html"


def post_view(request, id):
    """
    Display an individual :model:`feed.Post`.

    **Context**

    ``post``
        An instance of :model:`feed.Post`.

    **Template:**

    :template:`feed/post_view.html`
    """
    if request.method == "POST":
        print("Received a POST request")
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, id=id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.all().count()
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Posted')

    comment_form = CommentForm()
    print("About to render template")
    return render(
        request,
        "feed/post_view.html",
        {"post": post, "comments": comments, "comment_count": comment_count,
            "comment_form": comment_form, },
    )


def comment_edit(request, id, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error!')

    return HttpResponseRedirect(reverse('post_view', args=[id]))


def comment_delete(request, id, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, id=id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Not your comment!')

    return HttpResponseRedirect(reverse('post_view', args=[id]))
