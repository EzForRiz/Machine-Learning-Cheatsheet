# The Concat Function



# We sometimes need to collect data from different resources and combine them into a single DataFrame. How we approach this task depends on the characteristic of the data and the way it’s represented.

# One option is to combine them by stacking them side-by-side or on top of each other. We can imagine building a brick wall. One wall is made up of multiple bricks placed side-by-side and on top of one another. The concat function can be used for this task. Let’s go over some examples to learn how this function is used. Suppose we have the following DataFrames.


import pandas as pd

df1 = pd.DataFrame({"A":[1,5,3,2], "B":[11,6,9,6], "C":["a","d","f","b"]})

df2 = pd.DataFrame({"A":[2,4,1,7], "B":[14,9,5,8], "C":["b","b","j","a"]})

df_combined = pd.concat([df1, df2], axis=0)

print(df_combined)






# The indexes of the original DataFrames remain the same. To assign a new index to the resulting DataFrame, we need to set the ignore_index parameter as True. Note that the column names must match to combine them. The unmatched column names will also be present in the resulting DataFrame, but the values that come from the other DataFrame will be NaN.

# Let’s say we have the following two DataFrames.



import pandas as pd

df1 = pd.DataFrame({"A":[1,5,3,2], "B":[11,6,9,6], "C":["a","d","f","b"]})

df2 = pd.DataFrame({"A":[2,4,1,7], "B":[14,9,5,8], "D":["b","b","j","a"]})

df_combined = pd.concat([df1, df2], axis=0, ignore_index=True)

print(df_combined)




import pandas as pd

df1 = pd.DataFrame({"A":[1,5,3,2], "B":[11,6,9,6], "C":["a","d","f","b"]})

df2 = pd.DataFrame({"A":[2,4,1,7], "B":[14,9,5,8], "D":["b","b","j","a"]})

df_combined = pd.concat([df1, df2], axis=1)

print(df_combined)






import pandas as pd

df1 = pd.DataFrame({"A":[1,5,3,2], "B":[11,6,9,6], "C":["a","d","f","b"]})

df2 = pd.DataFrame({"A":[2,4,1,7], "B":[14,9,5,8], "D":["b","b","j","a"]},
                  index=[3,4,5,6])

df_combined = pd.concat([df1, df2], axis=1)

print(df_combined)






# The Merge Function



import pandas as pd

# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="left", on="product_code")

print(merged_df)





import pandas as pd

# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="inner", on="product_code")

print(merged_df)




import pandas as pd

# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="outer", on="product_code")

print(merged_df)