from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(max_length=125, unique=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts")
    update_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = ((0, 'Draft'), (1, 'Publish'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
