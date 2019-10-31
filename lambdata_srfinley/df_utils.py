"""utility functions for working with DataFrames"""

import pandas as pd

# dataframe to test break_date on
DATES = pd.DataFrame(data=[["6/15/1845"], ["11/01/1993"],
                           ["1/2/1934"], ["8/29/2000"]],
                     columns=["dates"])


# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
def break_date(df, col):
    """Break a column containing dates as strings into multiple columns

    Args:
        df: the dataframe with the column of dates
        col: the name of the column of dates
    Returns:
        a new dataframe without the original column of string dates, instead:
        -a column of datetimes called "dates" (or "date" if col="dates")
        -a column of the year values called "year"
        -a column of the month values called "month"
        -a column of the day values called "day"
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


# Single function to take a list, turn it into a series
# and add it to a dataframe as a new column
def add_column(df, ls, name):
    """Add a list as a new column to a dataframe.

    Args:
        df: the dataframe to have a new column appended
        ls: the list to be added as a column
        name: the name to be used for the new column
    Returns:
        new dataframe with the added column
    """
    df2 = df.copy()
    df2[name] = pd.Series(ls)
    return df2


class WrappedDF:
    """A class that contains a dataframe and some functions for it"""
    def __init__(self, df):
        self.df = df

    def get_height(self):
        """Return the height (number of rows) of the dataframe"""
        return self.df.shape[0]

    def get_width(self):
        """Return the width (number of columns) of the dataframe"""
        return self.df.shape[1]
