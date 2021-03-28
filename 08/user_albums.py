def make_album(name, title, nsongs=None):
    album = {}
    album['artist_name'] = name
    album['album_title'] = title

    if nsongs:
        album['number_of_songs'] = nsongs
    return album

while True:
    print("\nPlease input the artist name and album title:")
    print("(enter 'q' at any time to quit)")
    
    name = input("Artist name: ")
    if name == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    
    album = make_album(name, title)
    print(album)
