import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["name"].str[1::2])




import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["name"].str[0:3])




# structure : 
# str[start : end : step size] 





# Splitting
import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["name"].str.split(" "))



import pandas as pd

staff = pd.read_csv("staff.csv")

staff["last_name"] = staff["name"].str.split(" ", expand=True)[1]

print(staff[["name","last_name"]])









# combining
import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["name"] + " - " + staff["department"])






# Converting Strings to Upper and Lower Case


import pandas as pd

staff = pd.read_csv("staff.csv")

staff["name_lower"] = staff["name"].str.lower()

print(staff[["name","name_lower"]])

print(staff["department"].str.capitalize())

print(sales["department"][0].upper())







# : Create City and State Columns from the Address
import pandas as pd

staff = pd.read_csv("staff.csv")

def create_city_column():

  staff["state"] = staff["city"].str.split(", ", expand=True)[1]

  return list(staff["state"])




#   Replacing Characters in a String

import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["city"].str.replace(",", "-"))

# Create a state colum
staff["state"] = staff["city"].str[-2:]

# Replace state abbreviations with actual state names
staff["state"].replace(
    {"TX": "Texas", "CA": "California", "FL": "Florida", "GA": "Georgia"},
    inplace = True
)

print(staff["state"])







# Chained Operations

import pandas as pd

staff = pd.read_csv("staff.csv")

print(staff["city"].str.split(",", expand=True)[1].str.lower())

print(staff["department"].str.lower().replace("field quality","quality"))

print(staff.query("name > 'John Doe'").start_date.str[:4].astype("int"))







# : Make the Salary Column Proper

import pandas as pd

staff = pd.read_csv("staff.csv")

def make_salary_proper():
  try:
    staff["salary_cleaned"] = staff["salary"].str[1:].str.replace(",","") # Write your solution here
    staff["salary_cleaned"] = staff["salary_cleaned"].astype("int")
    return list(staff["salary_cleaned"])
  except:
    pass