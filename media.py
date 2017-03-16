class Movie:
	"""
	Encapsulates information about a single movie.

	Attributes:
		title (str):
			Title or name of the movie
		poster_image_url (str):
			URL to an image of the movie poster
		trailer_youtube_url (str):
			URL to a trailer for the movie hosted on YouTube
	"""

	def __init__(self, title, poster, trailer):
		"""
		Creates, initializes, and returns a new instance of a Movie,
		given its required information

		Args:
			title (str): Title or name of the movie
			poster (str): URL to an image of the movie poster
			trailer (str): URL to a trailer for the movie hosted on YouTube
		"""
		self.title = title
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer
