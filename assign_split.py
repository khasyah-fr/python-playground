import pandas as pd
import numpy as np

df = pd.read_csv('combined_asl.csv')

df_ok = df[(df['is_valid'] == True) & (df['is_duplicate'] == False)].copy()

df_ok["dataset_split"] = None

for category, group in df_ok.groupby('category'):
    group = group.sample(frac=1, random_state=42).reset_index()
    n = len(group)
    
    if n >= 3:
        n_test = max(1, int(np.floor(n * 0.15)))
        n_val = max(1, int(np.floor(n * 0.15)))
        n_train = n - n_test - n_val

        df_ok.loc[group.loc[:n_train-1, 'index'], "dataset_split"] = "train"
        df_ok.loc[group.loc[n_train:(n_train+n_val-1), 'index'], "dataset_split"] = "val"
        df_ok.loc[group.loc[n_train+n_val:, 'index'] , "dataset_split"] = "test"

    else:
        df_ok.loc[group['index'], "dataset_split"] = "train"

df_ok.to_csv('splitted_asl.csv')