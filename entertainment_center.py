import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
			"https://upload.wikimedia.org/wikipedia/en/6/6c/Toy_Story_3_Cover_Art.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")
						
pulp_fiction = media.Movie("Pulp Fiction",
			"https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
			"https://www.youtube.com/watch?v=s7EdQ4FqbhY")
						
the_lion_king = media.Movie("The Lion King",
			"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
			"https://www.youtube.com/watch?v=4sj1MT05lAA")
						
#make an empty list, append movies to it
movies = []
movies.append(toy_story)
movies.append(pulp_fiction)
movies.append(the_lion_king)

fresh_tomatoes.open_movies_page(movies)
