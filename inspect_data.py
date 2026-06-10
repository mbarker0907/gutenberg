import pandas as pd

# Load just the first 100 rows to avoid crashing
# We use 'on_bad_lines' to handle messy rows
df = pd.read_csv('data/raw/pg_catalog.csv.gz', nrows=100, on_bad_lines='warn')

# Print the column names and the first few rows
print("--- COLUMN NAMES ---")
print(df.columns.tolist())
print("\n--- FIRST ROW PREVIEW ---")
print(df.head(1))

# Check info to see what data types (numbers vs text) it detected
print("\n--- DATA TYPES ---")
print(df.info())