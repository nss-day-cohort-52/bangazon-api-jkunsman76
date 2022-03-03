from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    liked = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='liked')
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes")
   
