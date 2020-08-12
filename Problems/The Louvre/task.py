class Painting:
    museum = "the Louvre"

    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year


painting = Painting(input(), input(), input())

print('"{1}" by {0} ({2}) hangs in the Louvre.'.format(painting.title, painting.artist, painting.year))
