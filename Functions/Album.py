def make_album (artist_name, album_title, number_tracks= None):
    album = {"Artist name": artist_name.title(), "Album Title": album_title.title()}
    if number_tracks:
        album["Number of Tracks"]= number_tracks
    return album

print(make_album("Michael Jackson", "Fummble", 2))
print(make_album("Shiru wa G.p", "muaki"))
print(make_album("hillsong", "oceans"))

