"""
utility functions for working with DataFrames
"""

import pandas as pd

#dataframe to test break_date on
DATES = pd.DataFrame(data=[["6/15/1845"],["11/01/1993"],["1/2/1934"],["8/29/2000"]],columns=["dates"])

#Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
def break_date(df,col):
    """
    Takes a dataframe and the name of a column in it that consists of date-formatted strings. 
    Returns a copy of that dataframe, but without the original dates column, 
    and including the column of datetimes, as well as the three columns of ints for year, month, and day.
    """
    df2 = df.copy()
    date_col = 'dates'
    if col == 'dates':
        date_col = 'date'
    df2[date_col] = df2[col].apply(pd.to_datetime)
    df2['year'] = df2[date_col].apply(lambda d: d.year)
    df2['month'] = df2[date_col].apply(lambda d: d.month)
    df2['day'] = df2[date_col].apply(lambda d: d.day)
    df2 = df2.drop(columns=col)
    return df2

#Single function to take a list, turn it into a series and add it to a dataframe as a new column
def add_column(df,ls,name):
    df2 = df.copy()
    df2[name] = pd.Series(ls)
    return df2