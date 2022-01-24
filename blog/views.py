from django.views import generic
from blog.models import Post
from django.utils import timezone


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = "index.html"


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
