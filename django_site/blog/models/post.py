from django.db import models
from django.contrib.auth.models import User

status = (
    (0, 'Draft'),
    (3,'Publish')
)

class Post(models,Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugFields(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-create_on']

    def __str__(self):
        return self.title
