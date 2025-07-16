import pandas as pd

#dataFile = pd.read_excel("test_data.xlsx")
dataFile = pd.read_excel("test_data.xlsx", sheet_name="Sheet2")
print(dataFile)

json_data_file = pd.read_json("user.json")
print(json_data_file)
