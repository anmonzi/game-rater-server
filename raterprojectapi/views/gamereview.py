"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterprojectapi.models import Review, Player, Game



class ReviewView(ViewSet):
    """Game rater reviews"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        player = Player.objects.get(user=request.auth.user)

        # Create a new Python instance of the Review class
        # and set its properties from what was sent in the
        # body of the request from the client.
        review = Review()
        review.review = request.data["review"]
        review.player = player

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameId` in the body of the request.
        game = Game.objects.get(pk=request.data["game"])
        review.game = game
        # Try to save the new game to the database, then
        # serialize the game instance as JSON, and send the
        # JSON as a response to the client request
        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request':request})
            return Response(serializer.data)
        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        reviews = Review.objects.all()
        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)



class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    Arguments: serializer type
    """
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
