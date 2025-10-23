from schema.records import record


#Searchs for records (albums) using the authenticated spotifyt client (sp).
#The spotify client will utilize the query and output 'limit' number of relative records.
def search_records(sp, query, lim):
    results = sp.search(q = query, type = 'album', limit = lim) #completes search
    records = []

    for item in results['albums']['items']:
        album_data = {
            "name": item["name"],
            "release_date": item["release_date"],
            "total_tracks": item["total_tracks"],
            "artist_genre": "Unknown"
            }
        
        #Getting Genre
        artist_id = item["artists"][0]["id"] #gets actual artist id assigned by spotify
        artist_info = sp.artist(artist_id)   #gets info about artists of record using acutal spotify assigned artist_id
        genres = artist_info.get("genres", [])
        if genres: #check genres is populated
            album_data["artist_genre"] = genres[0]

        r = record(album_data) #creates a instant of the found data for a record 
        r.artist_id = artist_id
        records.append(r)

    return records

