# Pandas Date and Time Data Types

import pandas as pd

mydate = pd.to_datetime("2021-11-10")

first_date = pd.to_datetime("2021-10-10")
second_date = pd.to_datetime("2021-10-02")

diff = first_date - second_date

print(diff)

print(mydate)


print(type(diff))
print("\n")
print(diff.days)




staff = pd.read_csv("staff.csv")

staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]",
})

print(staff.dtypes)




# Dates include lots of information

import pandas as pd

mydate = pd.to_datetime("2021-10-10")

print(f"The year part is {mydate.year}")
print(f"The month part is {mydate.month}")
print(f"The week number part is {mydate.week}")
print(f"The day part is {mydate.day}")



mydate = pd.to_datetime("2021-10-10 14:30:00")

print(f"The hour part of mydate is {mydate.hour}")
print(f"The minute part of mydate is {mydate.minute}")
print(f"The second part of mydate is {mydate.second}")





# Methods instead of attributes

import pandas as pd

mydate = pd.to_datetime("2021-12-21 00:00:00")

print(f"The date part is {mydate.date()}")
print(f"The day of week is {mydate.weekday()}")
print(f"The name of the month is {mydate.month_name()}")
print(f"The name of the day is {mydate.day_name()}")






# The dt Accessor

# How to work with dates in a DataFrame
import pandas as pd

# read DataFrame
staff = pd.read_csv("staff.csv")

# change the data type of date columns
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]",
})

# create start_month column
staff["start_month"] = staff["start_date"].dt.month

print(staff[["start_date","start_month"]])





# dt.day vs. dt.days 
import pandas as pd

# Creating a datetime Series
date_series = pd.Series(pd.to_datetime(["2024-02-10", "2024-05-15", "2024-08-20"]))

# Extracting the day of the month
date_series_day = date_series.dt.day

# Displaying the result
print(date_series_day)




import pandas as pd

# Creating a DataFrame with two date columns
df = pd.DataFrame({
    "Start Date": pd.to_datetime(["2024-01-01 10:30:00", "2023-06-15 15:45:00"]),
    "End Date": pd.to_datetime(["2024-02-10 08:15:00", "2023-12-25 22:30:00"])
})

# Subtracting dates
df["Date Difference"] = df["End Date"] - df["Start Date"]

print(df["Date Difference"].dt.days)






# Manipulating Dates by Adding Time Intervals

import pandas as pd

# create the DataFrame
staff = pd.read_csv("staff.csv")

# change the date type
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

# create raise_date column
staff["raise_date"] = staff["start_date"] + pd.DateOffset(years=1)

print(staff[["start_date","raise_date"]].head())



# staff["start_date"] + pd.DateOffset(months=6)





import pandas as pd

mytime = pd.Timestamp("2021-12-14 16:50:00")

print("The first method")
print(mytime + pd.DateOffset(hours=-2))

print("\nThe second method")
print(mytime - pd.DateOffset(hours=2))




# Timedelta function

import pandas as pd

# create the DataFrame
staff = pd.read_csv("staff.csv")

# change the date type
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

# add 12 weeks
print(staff["start_date"] + pd.Timedelta(value=12, unit="W"))




import pandas as pd

# create the DataFrame
staff = pd.read_csv("staff.csv")

# change the date type
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

# add 12 weeks
print(staff["start_date"] + pd.Timedelta("12 W"))







# The Age of Employees

import pandas as pd

staff = pd.read_csv("staff.csv")

staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

def find_age():
    try:
    
        staff["age"] = (staff["start_date"] - staff["date_of_birth"]).dt.days / 365
        # convert to integer
        staff["age"] = staff["age"].astype("int")
        return list(staff["age"])
        
    except:
        pass