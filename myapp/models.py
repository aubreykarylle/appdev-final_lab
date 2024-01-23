# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.post.title} - {self.text}"

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
