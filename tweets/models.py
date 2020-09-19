import random
from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(upload_to='images/',blank=True,null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content, 
            "likes": random.randint(0,200)
        }