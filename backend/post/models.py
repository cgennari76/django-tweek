from django.db import models

class Post(models.Model):
    post = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post