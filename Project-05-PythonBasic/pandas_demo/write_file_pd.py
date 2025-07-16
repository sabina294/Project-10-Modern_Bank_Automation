import pandas as pd

data  = {
    "Name" : ["Alice","Smith","David"],
    "Age" :[20,30,40],
    "City": ["New York", "Paris", "London"]
}
df = pd.DataFrame(data)
print(df)

df.to_excel("users.xlsx",index=False)
df.to_csv("users.csv",index=False)
df.to_json("userJ.json")