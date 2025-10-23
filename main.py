from spotify.client import get_spotify_client
from spotify.fetch import search_records
from utils.export import export_record_list

#SetUp
sp = get_spotify_client()   #this is the authenticated spotify client


#Record Fetch
query = "Jazz & Blues"
limit = 50

records = search_records(sp, query, limit) #Performs fetch in spotify datatbase

#Export to CSV
export_record_list(records, "data/records.csv")