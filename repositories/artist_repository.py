from db.run_sql import run_sql
from models.artist import Artist 

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)

def find_artist(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['title'], result['id'])
    return artist

def select_all():
    artists = [] 
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(result['title'], result['id'])
        artists.append(artist)
    return artists 

def update(id):
    sql = "UPDATE artists SET (name, id) = (%s, %s) WHERE id = %s"
    values = [task.name, task.id]
    run_sql(sql, values) 


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s" 
    values = [id]
    run_sql(sql, values)