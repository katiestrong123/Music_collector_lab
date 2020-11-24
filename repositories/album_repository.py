from db.run_sql import run_sql
from models.album import Album 

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def find_album(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
    return album


def select_all():
    albums = [] 
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
        albums.append(album)
    return albums 

def select_all(artist):
    albums = [] 
    sql = "SELECT * FROM artists WHEN artist = artist"
    results = run_sql(sql)
    for row in results:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
        albums.append(album)
    return albums  

def update(id):
    sql = "UPDATE albums SET (title, genre, artist, id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.title, task.genre, task.artist, task.id]
    run_sql(sql, values) 

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s" 
    values = [id]
    run_sql(sql, values)
