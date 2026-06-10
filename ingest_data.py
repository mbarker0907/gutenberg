import os
import time
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load database credentials
load_dotenv()
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@localhost:5432/{os.getenv('DB_NAME')}"

# Configuration
FILE_PATH = 'data/raw/pg_catalog.csv.gz'
CHUNK_SIZE = 5000  # Process 5,000 rows at a time for efficiency
COLUMN_MAP = {
    'Text#': 'text_id',
    'Type': 'type',
    'Issued': 'issued',
    'Title': 'title',
    'Language': 'language',
    'Authors': 'authors',
    'Subjects': 'subjects',
    'LoCC': 'locc',
    'Bookshelves': 'bookshelves'
}

def ingest_data():
    engine = create_engine(db_url)
    start_time = time.time()
    total_rows = 0
    
    print("Starting full ingestion...")
    
    # Process the file in chunks to keep memory usage low
    for chunk in pd.read_csv(FILE_PATH, chunksize=CHUNK_SIZE, on_bad_lines='skip'):
        # Rename columns
        chunk = chunk.rename(columns=COLUMN_MAP)
        
        # Upload chunk to the database
        chunk.to_sql('raw_books', engine, if_exists='append', index=False)
        
        total_rows += len(chunk)
        print(f"Ingested {total_rows} rows so far...")
        
    duration = time.time() - start_time
    print(f"\nSuccess! Ingested {total_rows} entries in {duration:.2f} seconds.")

if __name__ == "__main__":
    ingest_data()