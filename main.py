import numpy as np
import pandas as pd

def main():
    print("Looping")
    for i in range(5):
        print(f"Iteration {i}")

    print("Numpy array")
    arr = np.array([[1,2,3], [4,5,6]])
    print(arr)

    print("Pandas DataFrame")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25,30,35],
        'Score': [85.5, 90.0, 92.5]
    }
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()
    