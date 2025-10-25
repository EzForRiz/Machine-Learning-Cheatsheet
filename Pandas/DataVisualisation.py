# Histogram

import pandas as pd
import matplotlib.pyplot as plt

grocery = pd.read_csv("grocery.csv")

grocery["price"].plot(kind="hist")

plt.savefig('output/abc.png')




import pandas as pd
import matplotlib.pyplot as plt

grocery = pd.read_csv("grocery.csv")

grocery["price"].plot(
    kind = "hist",
    figsize = (10, 6),
    title = "Histogram of grocery prices",
    xticks = [2,3,4,5,6,7,8,9,10,11,12]
)

plt.savefig('output/abc.png')





# Line Plot

import pandas as pd
import matplotlib.pyplot as plt

grocery = pd.read_csv("grocery.csv")

grocery[grocery["product_description"]=="tomato"].plot(
    x = "sales_date", 
    y = "sales_quantity",
    kind = "line",
    figsize = (10,5),
    title = "Daily tomato sales",
    #xlabel = "Sales date",
    #ylabel = "Sales quantity"
)

plt.savefig('output/abc.png')




import pandas as pd
import matplotlib.pyplot as plt

grocery = pd.read_csv("grocery.csv")

grocery[grocery["product_description"]=="tomato"].plot(
    x = "sales_date", 
    y = ["sales_quantity", "price"],
    kind = "line",
    figsize = (10,5),
    title = "Daily tomato sales and prices",
    secondary_y = "price"
)

plt.savefig('output/abc.png')






# Scatter Plot
import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales[["product_code","product_group","price","cost"]].head())


import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")

sales.plot(
    x = "price",
    y = "cost",
    kind = "scatter",
    figsize = (8, 5),
    title = "Cost vs Price"
)

plt.savefig('output/abc.png')




import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")

sales.plot(
    x = "price",
    y = "cost",
    kind = "scatter",
    figsize = (8, 5),
    title = "Cost vs Price",
    xlim = (0, 1000),
    ylim = (0, 800),
    grid = True
)

plt.savefig('output/abc.png')