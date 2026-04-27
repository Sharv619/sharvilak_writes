# TODO: re-enable LoginRequiredMixin, UserPassesTestMixin when adding auth
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):  # TODO: add LoginRequiredMixin later
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # TODO: replace with self.request.user when auth is enabled
        form.instance.author = User.objects.first()
        return super().form_valid(form)


class PostUpdateView(UpdateView):  # TODO: add LoginRequiredMixin, UserPassesTestMixin later
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView):  # TODO: add LoginRequiredMixin, UserPassesTestMixin later
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
