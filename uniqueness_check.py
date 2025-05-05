import pandas as pd

# Define data
data = [
    {"type": "WLASL", "url": "youtube.com/a", "category": "book", "frame_start": 0, "frame_end": 10, "is_duplicate": False},
    {"type": "WLASL", "url": "youtube.com/b", "category": "hello", "frame_start": 0, "frame_end": 10, "is_duplicate": False},
    {"type": "MSASL", "url": "youtube.com/a", "category": "book", "frame_start": 0, "frame_end": 10, "is_duplicate": False},
    {"type": "MSASL", "url": "youtube.com/a", "category": "book", "frame_start": 11, "frame_end": 20, "is_duplicate": False},
    {"type": "MSASL", "url": "youtube.com/c", "category": "thanks", "frame_start": 0, "frame_end": 10, "is_duplicate": False},
    {"type": "MSASL", "url": "youtube.com/c", "category": "thanks", "frame_start": 11, "frame_end": 20, "is_duplicate": False}
]

df = pd.DataFrame(data)

df['is_duplicate'] = df.duplicated(subset=['url', 'category', 'frame_start', 'frame_end'], keep='first')

uniqueness_dict = {}

# Populate dict with WLASL first
for _, row in df.iterrows():
    if row["type"] == 'WLASL':
        key = f"WLASL-{row['category']}-{row['url']}"
        uniqueness_dict[key] = uniqueness_dict.get(key, 0) + 1

# Check MSASL against WLASL
for index, row in df.iterrows():
    if row["type"] == 'MSASL' and row["is_duplicate"] == False:
        key = f"WLASL-{row['category']}-{row['url']}"
        if uniqueness_dict.get(key, 0) > 0:
            df.at[index, 'is_duplicate'] = True

# Output the resulting DataFrame
print(df)
