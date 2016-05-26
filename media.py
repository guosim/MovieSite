import webbrowser

class Movie():
	# constructor, creates an instance of a movie 
	# object given title, boxart and trailer
	def __init__(self, title, boxart, trailer):
		self.title = title
		self.poster_image_url = boxart
		self.trailer_youtube_url = trailer
		
	# opens an instance's trailer
	def show_trailer(self):
		webbrowser.open(self.trailer)
