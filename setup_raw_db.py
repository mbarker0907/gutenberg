import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def create_raw_table():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host='localhost'
    )
    cur = conn.cursor()
    
    # DROP the old table first so we can recreate it cleanly
    cur.execute("DROP TABLE IF EXISTS raw_books;")
    
    # Note: Using lowercase column names consistently
    query = '''
    CREATE TABLE raw_books (
        text_id INTEGER PRIMARY KEY,
        type TEXT,
        issued TEXT,
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
    print("Table 'raw_books' recreated successfully with correct schema!")

if __name__ == "__main__":
    create_raw_table()