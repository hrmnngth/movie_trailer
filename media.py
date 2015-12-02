import webbrowser


class Movie():
        # Arguments defined as string, only the image argument is an object from Image class

    def __init__(self, movie_title, movie_story_line, image,
                 trailer_youtube_url, production_company,
                 movie_release_date, movie_location):
        self.title = movie_title
        self.story_line = movie_story_line
        self.image_object = image 	# An instance of object Image
        self.trailer_youtube_url = trailer_youtube_url
        self.production_company = production_company
        self.release_date = movie_release_date
        self.location = movie_location


class Image():
        # Arguments defined as string

    def __init__(self, poster_image_url, width_size, height_size):
        self.poster_image_url = poster_image_url
        self.width_size = width_size
        self.height_size = height_size
