from objects import records

class user:
    def __init__(self, name):
        self.name = name
        self.id = ""
        self.record_Title = []

    def assign_id(self, id):
        self.id = id

    def add_record(self, record: records):
        self.record_Title.append(record.album.name)