import pandas as pd

table = pd.read_excel('C:\\Users\\rbotha.SYMOK\\Desktop\\Programming\\Copies for denise.xlsx',
                  sheet_name = 'Sheet1',
                  header = 0,
                  index_col = 0,
                  usecols = "B",
                  convert_float = True)
                 
print(table)

