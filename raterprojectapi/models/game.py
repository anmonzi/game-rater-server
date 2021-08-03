from django.db import models
from django.db.models.fields import DateField


class Game(models.Model):
    """Game Model"""

    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = DateField()
    number_of_players = models.IntegerField()
    game_time = models.IntegerField()
    age_rec = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="category")
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
