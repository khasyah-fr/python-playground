import pandas as pd

# Initialize base DataFrame with column dtypes
df = pd.DataFrame({
    "id": pd.Series(dtype='int'),
    "category": pd.Series(dtype='str'),
    "category_num": pd.Series(dtype='int'),
    "dataset_type": pd.Series(dtype='str'),
    "url": pd.Series(dtype='str'),
    "dataset_split": pd.Series(dtype='str'),
    "frame_start": pd.Series(dtype='int'),
    "frame_end": pd.Series(dtype='int'),
    "fps": pd.Series(dtype='float'),
    "filename": pd.Series(dtype='str'),
    "is_valid": pd.Series(dtype='bool'),
    "is_duplicate": pd.Series(dtype='bool'),
})

ms_asl_json = pd.read_json("MSASL_test.json")

rows = []
category_counts = {}  # Cache to count per category

counter = len(df)

for _, row in ms_asl_json.iterrows():
    category = row["clean_text"]
    category_counts[category] = category_counts.get(category, 0) + 1

    new_row = {
        "id": counter + 1,
        "category": category,
        "dataset_type": "MSASL",
        "url": row["url"],
        "dataset_split": "", #TODOsplit 
        "frame_start": row["start"],
        "frame_end": row["end"],
        "fps": row["fps"],
        "filename": f"{counter+1}.mp4",
        "is_valid": None, #TODOchecked
        "is_duplicate": None, #TODOchecked
    }
    rows.append(new_row)
    counter += 1

# Add all rows at once
df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

# Export to CSV
df.to_csv("MSASL_test.csv", index=False)
