from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title