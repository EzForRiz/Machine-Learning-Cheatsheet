def analyzeData():
    import seaborn as sns
    import pandas as pd

    # Load the dataset
    diamonds = sns.load_dataset('diamonds')

    # Count the number of unique color values
    color = diamonds['color'].nunique()

    return color


# dataset isnt loaded rn but u can find one online from kaggel or something


# Access the diamonds dataset from the seaborn library and use the pandas library to tell the number of distinct (unique) color variables in the diamonds dataset?

# def analyzeData(): 
    # All required libraries are already imported with default alias 
    # Write your code here 
    # color = # number of distinct colors (#save your answer in this variable) 
    # return color 
    # return your answer pass Recall the pandas function used to count unique values.