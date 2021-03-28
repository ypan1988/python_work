def make_album(name, title, nsongs=None):
    album = {}
    album['artist_name'] = name
    album['album_title'] = title

    if nsongs:
        album['number_of_songs'] = nsongs
    return album

album1 = make_album('Jay Chou', "Jay's Fantasy")
print(album1)
album2 = make_album('Jay Chou', 'Yeh Hui-mei')
print(album2)
album3 = make_album('Jat Chou', 'Still Fantasy')
print(album3)

album4 = make_album('Stefanie Sun', 'Kite', 10)
print(album4)
