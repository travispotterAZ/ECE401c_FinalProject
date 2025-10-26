import time #for runtime

from spotify.client import get_spotify_client   #authentication
from spotify.fetch import search_ALBUMS_by_artists       #search spotify database
from utils.export import export_record_list     #exporting to csv

PopularGenres = ["pop", "hip-hop", "rock", "country", "edm", "latin", "k-pop", "R&B/Soul", "jazz", "classical", "reggae", "indie", "folk", "metal", "blues"]
allRecords = []
#SetUp
sp = get_spotify_client()   #this is the authenticated spotify client

#Search_time Start
start_time = time.time()

#Record Fetch
query = ""
limit = 50

for genre in PopularGenres:
    records = search_ALBUMS_by_artists(sp, query = genre, artist_lim = 50) #Performs fetch in spotify datatbase
    allRecords.extend(records)


#Search_time end
end_time = time.time()
search_time = end_time - start_time
print(f"Exported {len(allRecords)} records to data/records.csv")
print(f"Runtime: {search_time:.2f} seconds")

#Export to CSV
export_record_list(allRecords, "data/records.csv")