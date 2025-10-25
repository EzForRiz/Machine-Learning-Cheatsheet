import pandas as pd

grocery = pd.read_csv("grocery.csv")

print("The size of the DataFrame:")
print(grocery.shape)

print("\nThe column names are:")
print(list(grocery.columns))

print("\nThe first five rows:")
print(grocery.head())





# groupby function
import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(grocery.groupby("product_group").mean())




import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(grocery[["product_group","price"]].groupby("product_group").mean())




# Enhancing the groupby Function

import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(
  grocery.groupby("product_group").agg(
    avg_price = ("price","mean")
  )
)


import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(
  grocery.groupby("product_group").agg(
    avg_price = ("price","mean"),
    total_sales = ("sales_quantity", "sum")
  )
)



import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(
  grocery.groupby("product_description").agg(
    avg_price = ("price","mean"),
    total_sales = ("sales_quantity", "sum")
  ).sort_values(
    by="total_sales",
    ascending=False
  )
)




import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(
  grocery.groupby(
    ["product_description", "product_group"]
  ).agg(
    avg_price = ("price","mean"),
    total_sales = ("sales_quantity", "sum")
  )
)




# Find the Weekly Sales Quantities
import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(grocery.head())


import pandas as pd

grocery = pd.read_csv("grocery.csv")

grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")

def find_weekly_sales():
  try:
    grocery["week"] = grocery["sales_date"].dt.week
    result = grocery.groupby("week").agg(
      total_sales = ("sales_quantity","sum")
    ).sort_values(by="total_sales", ascending=False)

    return list(result["total_sales"])
  except:
    pass






# Pivot Table Function

import pandas as pd

grocery = pd.read_csv("grocery.csv")

# Creating the week column
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = grocery["sales_date"].dt.week

# Creating the pivot table
print(
  pd.pivot_table(
    data = grocery, 
    values = "sales_quantity", 
    index = "product_group", 
    columns = "week",
    aggfunc = "sum"
  )
)



import pandas as pd

grocery = pd.read_csv("grocery.csv")

# Creating the week column
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = grocery["sales_date"].dt.week

# Creating the pivot table
print(
  pd.pivot_table(
    data = grocery, 
    values = "price", 
    index = "week", 
    columns = "product_group",
    aggfunc = ["mean","std"]
  )
)




import pandas as pd

grocery = pd.read_csv("grocery.csv")

# Creating the week column
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = grocery["sales_date"].dt.week

# Creating the pivot table
print(
  pd.pivot_table(
    data = grocery, 
    values = "sales_quantity", 
    index = "product_group", 
    columns = "week",
    aggfunc = "sum",
    margins = True,
    margins_name = "Total"
  )
)




# The Cut and Qcut Functions


import pandas as pd

# Create a Series with values between 0 and 10
A = pd.Series([5, 0, 2, 8, 4, 10, 7])

# cut function
A_binned = pd.cut(A, bins=4)

print(A_binned)



import pandas as pd

# Create a Series with values between 0 and 10
A = pd.Series([5, 0, 2, 8, 4, 10])

# cut function
A_binned = pd.cut(A, bins=[-1, 3, 6, 10], labels=["small","medium","large"])

print(A_binned)
print("\n")
print(A_binned.value_counts())





import pandas as pd

# Create a Series
A = pd.Series([1, 4, 2, 10, 5, 6, 8])

# The qcut function
A = pd.Series([1, 4, 2, 10, 5, 6, 8, 7, 5, 3, 5, 9])

A_binned = pd.qcut(A, q=3)

print(A_binned.value_counts())






import pandas as pd

A = pd.Series([1, 4, 2, 10, 5, 6, 8])

# The qcut function
A = pd.Series([1, 4, 2, 3, 10, 5, 6, 8, 7, 5, 9, 14])

A_binned = pd.qcut(A, q=[0, 0.50, 0.75, 1])

print(A_binned.value_counts())






# Categorize Groceries Based on Price



import pandas as pd

grocery = pd.read_csv("grocery.csv")

def find_avg_price():
  try:
    grocery["price_category"] = pd.cut(
      grocery["price"],
      bins = 3,
      labels = ["cheap", "mid-priced", "expensive"]
    )

    avg_prices = grocery.groupby("price_category").agg(
      avg_price = ("price", "mean")
    )

    return list(avg_prices.index), list(avg_prices["avg_price"].round(2))
  except:
    pass




# The "where" Function



import pandas as pd

grocery = pd.read_csv("grocery.csv")

grocery["price_updated"] = grocery["price"].where(
  grocery["price"] >= 3,
  other = grocery["price"] * 1.1
)

print("Checking prices less than $3:")
print(grocery[grocery["price"] < 3][["price","price_updated"]].head())

print("\nChecking prices of $3 or more:")
print(grocery[grocery["price"] >= 3][["price","price_updated"]].head())





import pandas as pd

grocery = pd.read_csv("grocery.csv")

grocery["price_updated"] = grocery["price"].where(
  grocery["product_group"] != "vegetable",
  other = grocery["price"] * 0.9
)

print("Checking prices of vegetables:")
print(grocery[grocery["product_group"] == "vegetable"][["price","price_updated"]].head())

print("\nChecking prices of other products:")
print(grocery[grocery["product_group"] != "vegetable"][["price","price_updated"]].head())