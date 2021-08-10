"""View module for handling requests about ratings"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterprojectapi.models import Game, Player, Rating



class RatingView(ViewSet):
    """Game rater ratings"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        player = Player.objects.get(user=request.auth.user)
        # Create a new Python instance of the Game class
        # and set its properties from what was sent in the
        # body of the request from the client.
        rating = Rating()
        rating.rating = request.data["rating"]
        rating.player = player
        game = Game.objects.get(pk=request.data["game"])
        rating.game = game

        try:
            rating.save()
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all ratings from the database
        ratings = Rating.objects.all()

        # That URL will retrieve all reviews from game 1
        game = self.request.query_params.get('game', None)
        if game is not None:
            ratings = Rating.objects.filter(game__id=game)
        # alternative ORM method
        # game = self.request.query_params.get('game', None)

        # if game:
        #     ratings = Rating.objects.filter(game=game)
        # else:
        #     ratings = Rating.objects.all()

        serializer = RatingSerializer(ratings, many=True, context={'request': request})
        return Response(serializer.data)


class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    Arguments: serializer type
    """
    class Meta:
        model = Rating
        fields = '__all__'
        depth = 1

