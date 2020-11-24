from db.run_sql import run_sql
from models.artist import Artist 

def save(artist):
    sql = "INSERT INTO artist (name) VALUES %s RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = id
    return artist