class Movie:

    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Rating:

    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Link:

    def __init__(self, movieId, imdbld, tmdbld):
        self.movieId = movieId
        self.imdbld = imdbld
        self.tmdbld = tmdbld


class Tag:

    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
