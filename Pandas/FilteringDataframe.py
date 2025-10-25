import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.loc[:4, ["product_code","product_group"]])





import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.iloc[[5,6,7,8], [0,1]])

print(sales.iloc[5:9, :2])






import numpy as np
import pandas as pd

df = pd.DataFrame(
  np.random.randint(10, size=(4,4)),
  index = ["a","b","c","d"],
  columns = ["col_a","col_b","col_c","col_d"]
  )

print(df)

print("\nSelect two rows and two columns using loc:")
print(df.loc[["b","d"], ["col_a","col_c"]])








import pandas as pd

sales = pd.read_csv("sales.csv")

selected_columns = ["product_code","price"]

print(sales[selected_columns].head())









import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales["product_code","price"].head())










import pandas as pd

# read the sales csv file
sales = pd.read_csv("sales.csv")

# filter the sales data frame
sales_filtered = sales[(sales["price"] > 100) & (sales["stock_qty"] < 400)]

print(sales_filtered[["price","stock_qty"]].head())









import pandas as pd

sales = pd.read_csv("sales.csv")

sales_filtered = sales.query("price > 100 and stock_qty < 400")

print(sales_filtered[["product_code","price","stock_qty"]].head())







import pandas as pd

sales = pd.read_csv("sales.csv")

def find_the_number_of_products():
    try:
        average_price = sales["price"].mean() # find the mean value of the price column
        sales_filtered = sales[sales["price"] > average_price] # filter the products that have a price higher than the average price
        number_of_products = sales_filtered["product_code"].nunique() # find the number of unique product codes in sales_filtered
        
        return number_of_products
    except:
    pass