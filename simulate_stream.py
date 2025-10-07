import pandas as pd
import time
import os

# Ensure output directory exists
os.makedirs("streaming_data", exist_ok=True)

# Load full dataset
df = pd.read_csv("cfpb_all_complaints.csv")

# Write chunks of 100 rows every 5 seconds
chunk_size = 100
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i+chunk_size]
    file_path = f"streaming_data/data_{i}.json"
    chunk.to_json(file_path, orient='records', lines=True)
    print(f"Wrote chunk: {file_path}")
    time.sleep(5)
