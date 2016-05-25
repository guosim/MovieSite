import webbrowser

class Movie():
	def __init__(self, title, boxart, trailer):
		self.title = title
		self.poster_image_url = boxart
		self.trailer_youtube_url = trailer
		
	def show_trailer(self):
		webbrowser.open(self.trailer)


#To help you generate a website that displays these movies, we have provided a Python module called
# fresh_tomatoes.py - this module has a function called open_movies_page that takes in one argument,
# which is a list of movies and creates an HTML file which visualizes all of your favorite movies.