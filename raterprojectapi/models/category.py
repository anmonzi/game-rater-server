from django.db import models


class Category(models.Model):
    """Category model"""

    label = models.CharField(max_length=50)
    