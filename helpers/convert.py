import pandas as pd
df = pd.read_excel("countries-legaldata.xlsx")
df.to_csv("country_data.csv", index=False)