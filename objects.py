class albums_list:
    def __init__(self, data):
        self.name = data['name']
        self.release_date = data['release_date']
        self.total_tracks = data['total_tracks']
        self.artist = data['artists'][0]['name']
    #


    def __repr__(self):
        return (f"Album(name={self.name}, "
                f"release_date={self.release_date}, "
                f"total_tracks={self.total_tracks}, "
                f"artist={self.artist})")
    #

class records:
    def __init__(self, data):
        self.album = albums_list(data['album'])
        self.rating = ""
        self.review = ""

    def __repr__(self):
        return (f"Record(album={self.album}, "
                f"rating={self.rating}, "
                f"review={self.review})")