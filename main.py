import pandas as pd
import spotipy                                          # Spotify Web API Wrapper   

from objects import albums_list as Album
from authentication import get_spotify_client
from users import *

sp = get_spotify_client()

# Get multiple albums (say top 5 Radiohead albums)
results = sp.search(q='Rock and Roll', type='album', limit=25)       #searches for # albums (limit) from artist Radiohead

# Convert each item into an Album object
albums = [Album(item) for item in results['albums']['items']]

print("\n")

# Print album details
#for i in range(len(albums)):
#	print(albums[i])
	
print("\n")
# Convert to DataFrame for better visualization
df = pd.DataFrame([album.__dict__ for album in albums])
print(df)
df.to_csv("albums.csv")    # Represents a Spotify Album 


#Make Users
user1 = user("Travis")
user2 = user("Andrew")
user3 = user("Rick")

#Assign IDs
user1.assign_id("00001")
user2.assign_id("00002")    
user3.assign_id("00003")

#Update Records
user1.add_record(albums[0])
user2.add_record(albums[1])
user3.add_record(albums[2])

#Add Review
user1.records[0].review = "Amazing album!"
user2.records[0].review = "A masterpiece!"
user3.records[0].review = "Not my favorite."

df = pd.DataFrame([user.__dict__ for user in [user1, user2, user3]])
print(df)
df.to_csv("users.csv")

print("\n")