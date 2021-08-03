from django.db import models


class Rating(models.Model):
    """Rating Model"""

    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    