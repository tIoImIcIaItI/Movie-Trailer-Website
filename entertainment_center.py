from fresh_tomatoes import open_movies_page
from media import Movie


def getAllMovies():
	"""
	Returns:
		An array of movies initialized with their supporting data.
	"""

	return [
		Movie(
			"Gladiator",
			"https://www.movieposter.com/posters/archive/main/22/A70-11370",
			"https://www.youtube.com/watch?v=DQc0lFrHICQ"),
		Movie(
			"Top Gun",
			"https://www.movieposter.com/posters/archive/main/15/A70-7600",
			"https://www.youtube.com/watch?v=qAfbp3YX9F0"),
		Movie(
			"The Matrix",
			"https://www.movieposter.com/posters/archive/main/9/A70-4902",
			"https://www.youtube.com/watch?v=m8e-FF8MsqU"),
	]


# Open the web page, passing in the list of movies to display
open_movies_page(
	getAllMovies())
