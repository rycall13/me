import pandas as pd

data = [
    {"Name": "Allyson", "Score": 85},
    {"Name": "Brian", "Score": 90},
    {"Name": "Charlie", "Score": 78},
    {"Name": "David", "Score": 92},
    {"Name": "Evelyn", "Score": 88},
    {"Name": "Jaden", "Score": 75},
    {"Name": "Grace", "Score": 95},
    {"Name": "Harold", "Score": 80},
    {"Name": "Ivy", "Score": 85},
    {"Name": "Jared", "Score": 89}
]


df = pd.DataFrame(data)


print(df["Name"])