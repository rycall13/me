import pandas as pd

df = pd.read_csv("locations.csv")

null_rows = df[df.isnull().any(axis=1)]

null_rows.to_csv("q1.out", index=False)

print("Null rows have been written to q1.out")
