from django.db import models
from django.db.models.fields import DateField
from .rating import Rating


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


    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        if total_rating == 0:
            return 0
        else:
            avg_rating = round((total_rating / len(ratings)), 2)
            return avg_rating

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.