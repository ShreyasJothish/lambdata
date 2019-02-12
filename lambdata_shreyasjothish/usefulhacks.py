"""
File name: usefulhacks.py
Developer: Shreyas Jothish
Description: Provides code snippets on useful coding hacks.
"""

class UsefulHacks:
    def __init__(self):
        self.help()

    def help(self):
        """
        This function returns list of function names with useful coding hacks snippets.
        """
        print('Here the code snippets assumes pandas and numpy are imported as given below')
        print('import pandas as pd')
        print('import numpy as np')
        print('df refers to pd.DataFrame object')
        print('col refers to column name within a df')
        print('row refers to row name within a df')
        print('------------------------------------------------------------------------------')
        print('Function names with useful coding hacks snippets')
        print('------------------------------------------------------------------------------')
        print('infinity_as_na: Consider infinity as na in Pandas.')
        print('unlimited_columns_display: Setting unlimited columns for display')
        print('unlimited_rows_display: Setting unlimited rows for display')
        print('select_numeric_columns: Selecting only numerical columns in DataFrame')
        print('display_data_instances: Display the number of instances of data within a column')
        print('log_transformation: Log transformation of a column')
    
    def infinity_as_na(self):
        """
        Code snippet for considering infinity as na in Pandas.
        """
        print('pd.options.mode.use_inf_as_na = True')

    def unlimited_columns_display(self):
        """
        Code snippet for setting unlimited columns for display
        """
        print("pd.set_option('display.max_columns', None)")

    def unlimited_rows_display(self):
        """
        Code snippet for setting unlimited rows for display
        """
        print("pd.set_option('display.max_rows', None)")

    def select_numeric_columns(self):
        """
        Code snippet for selecting only numerical columns in DataFrame
        """
        print('df.select_dtypes(include=np.number)')
    
    def display_data_instances(self):
        """
        Code snippet for displaying the number of instances of data within a column
        """
        print('df[col].value_counts()')

    def log_transformation(self):
        """
        Code snippet for log transformation of a column
        """
        print("np.log(df[col])")
