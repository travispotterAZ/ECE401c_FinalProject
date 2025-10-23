class record:
    def __init__(self, album_data): #defintion of record object
        self.record_id = -1 #FIX
        self.artist_id = -1
         #name is key in album_data dictionary
        self.title = album_data["name"]
        self.release_date = album_data["release_date"]
        self.total_tracks = album_data["total_tracks"]
        self.genre = album_data.get("artist_genre", "Unknown")  #default\

    def to_dictionary(self): #Converts 'record' object to dictionary - needed for use of pandas to get CSV
        return {
            "record_id": self.record_id,
            "artist_id": self.artist_id,
            "title": self.title,
            "release_date": self.release_date,
            "total_tracks": self.total_tracks,
            "artist_genre": self.genre
        }