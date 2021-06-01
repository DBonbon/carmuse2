from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm
from blog.models import Post, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog/blog_index.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_on']


def search(request):
    if request.method == "POST":
        search = request.POST['search']
        posts = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        context = {
                'search': search,
                'posts': posts,

        }

        return render(request, "blog/search.html", context)


    else:
        return render(request, "blog/search.html", {})


"""
def search(request):
    qeury=None
    results=[]
    if request.method=="POST":
        query = request.POST('search')
        results = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

       # pages = Paginator(request, num=10)
        context = {
            'query': query,
            'results': results,
        }
    return render(request, "blog/search.html", context)

"""

# todo convert the def (request) into class based structure.
#todo Comments how to incorperate them with CSS, collapsing windows and.../
# todo authors, logins, etc'

# The below structure functioned partially. It displayed the imeages, but not in the right place. 
# I use know Corey's n10 structure. 
# Which is only Post view and post detail. 


"""
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                content=form.cleaned_data["content"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/post_detail.html", context)

"""

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog/blog_category.html", context)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





