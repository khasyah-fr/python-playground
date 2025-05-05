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

ms_asl_train_json = pd.read_json("MSASL_train.json")
ms_asl_val_json = pd.read_json("MSASL_val.json")
ms_asl_test_json = pd.read_json("MSASL_test.json")

train_rows = []
val_rows = []
test_rows = []

# Process train rows
counter = len(df)
for _, row in ms_asl_train_json.iterrows():
    category = row["clean_text"]

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
    train_rows.append(new_row)
    counter += 1

df = pd.concat([df, pd.DataFrame(train_rows)], ignore_index=True)



# Process val rows
counter = len(df)
for _, row in ms_asl_val_json.iterrows():
    category = row["clean_text"]

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
    val_rows.append(new_row)
    counter += 1

df = pd.concat([df, pd.DataFrame(val_rows)], ignore_index=True)


# Process test rows
counter = len(df)
for _, row in ms_asl_test_json.iterrows():
    category = row["clean_text"]

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
    test_rows.append(new_row)
    counter += 1

# Add all rows at once
df = pd.concat([df, pd.DataFrame(test_rows)], ignore_index=True)

# is_duplicate should be False for the first unique [url, frame_start, frame_end], then True for others
df['is_duplicate'] = df.duplicated(subset=['url', 'frame_start', 'frame_end'], keep='first')

# Export to CSV
df.to_csv("MSASL.csv", index=False)
