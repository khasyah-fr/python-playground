import pandas as pd
import numpy as np

# Sample data
data = [
    {"dataset_type": "WLASL", "url": "youtube.com/a", "category": "book", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "WLASL", "url": "youtube.com/b", "category": "book", "is_valid": False, "is_duplicate": False},
    {"dataset_type": "WLASL", "url": "youtube.com/c", "category": "book", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "MSASL", "url": "youtube.com/d", "category": "book", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "MSASL", "url": "youtube.com/e", "category": "book", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "WLASL", "url": "youtube.com/x", "category": "hello", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "MSASL", "url": "youtube.com/y", "category": "hello", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "WLASL", "url": "youtube.com/z", "category": "hello", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "MSASL", "url": "youtube.com/z", "category": "hello", "is_valid": True, "is_duplicate": False},
    {"dataset_type": "MSASL", "url": "youtube.com/zz", "category": "hello", "is_valid": True, "is_duplicate": False},
]

df = pd.DataFrame(data)

# Filter for valid and non-duplicate
df_valid = df[(df["is_valid"] == True) & (df["is_duplicate"] == False)].copy()

# Apply per-category splitting
for category, group in df_valid.groupby("category"):
    group = group.sample(frac=1, random_state=42).reset_index()  # shuffle + keep original index
    n = len(group)

    if n >= 3:
        n_val = max(1, int(np.floor(n * 0.15)))
        n_test = max(1, int(np.floor(n * 0.15)))
        n_train = n - n_val - n_test

        df_valid.loc[group.loc[:n_train - 1, 'index'], "dataset_split"] = "train"
        df_valid.loc[group.loc[n_train:n_train + n_val - 1, 'index'], "dataset_split"] = "val"
        df_valid.loc[group.loc[n_train + n_val:, 'index'], "dataset_split"] = "test"
    else:
        df_valid.loc[group["index"], "dataset_split"] = "train"

print(df)