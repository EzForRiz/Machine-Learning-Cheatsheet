
import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.shape)

print(sales.size)

print(len(sales))




import pandas as pd

sales = pd.read_csv("sales.csv")

print("As index:")
print(sales.columns)

print("As list:")
print(list(sales.columns))




import pandas as pd

sales = pd.read_csv("sales.csv")

sales["stock_qty"] = sales["stock_qty"].astype("float")

print(sales.dtypes)





import pandas as pd

sales = pd.read_csv("sales.csv")

sales = sales.astype({
  "stock_qty": "float",
  "last_week_sales": "float"
})

print(sales.dtypes)





import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales["product_group"].nunique())

print(sales["product_group"].unique())




import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales["product_group"].value_counts())





import pandas as pd

sales = pd.read_csv("sales.csv")

print("mean: ")
print(sales["price"].mean())

print("median: ")
print(sales["price"].median())

print("mode: ")
print(sales["price"].mode()[0])

print("minimum: ")
print(sales["price"].min())

print("maximum: ")
print(sales["price"].max())








import pandas as pd

sales = pd.read_csv("sales.csv")

print("variance: ")
print(sales["price"].var())

print("standard deviation: ")
print(sales["price"].std())






import pandas as pd

sales = pd.read_csv("sales.csv")

def find_most_frequents(column_name):
  try:
    return list(sales[column_name].value_counts().index[0:3])
  except:
    pass