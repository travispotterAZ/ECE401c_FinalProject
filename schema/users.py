class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.records = []

    def add_record(self, album_data, review=""):
        self.records.append({
            "album_name": album_data["name"],
            "artist": album_data["artist"],
            "review": review
        })