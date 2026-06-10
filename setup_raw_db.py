import psycopg2

# Adjust these credentials to match your local PostgreSQL setup
DB_CONFIG = {
    "dbname": "library_db",
    "user": "barker",        # Change if your user is different
    "password": "NinaAlice", # Change to your actual password
    "host": "localhost",
    "port": "5432"
}

def create_raw_table():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # We define columns as TEXT to handle the messy data (commas, quotes)
    # until we decide how to clean it later.
    query = '''
    CREATE TABLE IF NOT EXISTS raw_books (
        text_id INTEGER PRIMARY KEY,
        type TEXT,
        issued DATE,
        title TEXT,
        language TEXT,
        authors TEXT,
        subjects TEXT,
        locc TEXT,
        bookshelves TEXT
    );
    '''
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("Table 'raw_books' initialized successfully!")

if __name__ == "__main__":
    create_raw_table()