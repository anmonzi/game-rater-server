from django.db import models


class GameImage(models.Model):
    """Game Image Model"""

    image = models.ImageField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    