import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.head())


import pandas as pd

sales = pd.read_csv("sales.csv", usecols=["product_code","product_group","stock_qty"])

print(sales.head())