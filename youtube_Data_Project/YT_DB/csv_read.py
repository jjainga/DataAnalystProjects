import pandas as pd

Categories = pd.read_csv('../Data/Youtube_Categories.csv',index_col=False, delimiter=',')

ytData = pd.read_csv('../Data/Youtube_Data.csv',index_col=False, delimiter=',')