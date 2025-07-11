from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True, blank=True)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} : {self.body[:20]}"