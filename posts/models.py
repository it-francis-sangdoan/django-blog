from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Archive"),
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(
        null=True,
        upload_to="post",
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
