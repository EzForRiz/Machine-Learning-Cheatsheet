#Series is a one-dimensional array with axis labels. There are multiple ways to create an array. Before exploring the examples, we’ll need to import Pandas.


import pandas as pd

myseries = pd.Series([10, 20, 30])

print(myseries)



import pandas as pd

myseries = pd.Series(
     [10,20,30], 
     index = ["a","b","c"]
)

print(myseries)

#By default, Series is assigned an integer index, but it can be changed using the index parameter.



import pandas as pd

myseries = pd.Series(
   ["Jane","John","Emily","Matt"]
)

# Print the first item
print(myseries[0])


import pandas as pd

myseries = pd.Series([1,2,3])
print(myseries.is_unique)



import pandas as pd

myseries = pd.Series([1,1,3])
print(myseries.is_unique)