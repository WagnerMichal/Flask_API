import sqlite3

def connect_db():
    connect = sqlite3.connect("movies.db")
    connect.row_factory = sqlite3.Row
    return connect


def create_tables():
    try:
        connect = connect_db()
        connect.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                release_year INTEGER NOT NULL
            );
        ''')
        connect.commit()
        print("Movie table created successfully")
    except:
        print("Movie table creation failed")
    finally:
        connect.close()