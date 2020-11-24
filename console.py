import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist('Car Seat Headrest')
artist_repository.save(artist_1)

artist_2 = Artist('DOPE LEMON')
artist_repository.save(artist_2)

artist_3 = Artist('IDLES')
artist_repository.save(artist_3)

album_1 = Album('Teens of Denial', 'Indie Rock', artist_1)
album_repository.save(album_1)

album_2 = Album('Honey Bones', 'Alternative/Indie', artist_2)
album_repository.save(album_2)

album_3 = Album('Brutalism', 'Rock', artist_3)
album_repository.save(album_3)

album_3 = Album('Joy as an Act of Resistance', 'Rock', artist_3)
album_repository.save(album_3)

pdb.set_trace()