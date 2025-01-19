def make_album (artist_name, album_title, number_tracks= None):
    album = {"Artist name": artist_name.title(), "Album Title": album_title.title()}
    if number_tracks:
        album ["Number of tracks"]= number_tracks
    return album



while True:
    print("Provide the artist's name and the name of the album")
    print("Enter 'q' at any point to quit!")
    artist = input("Enter the artist's name: ")
    album_name = input("Enter the album title: ")

    if artist.lower() == "q":
        break
    if album_name.lower()== "q":
        break

    user_album = make_album(artist, album_name)
    print(user_album)
