import pandas as pd

df = pd.read_csv('../data/raw/Car details v3.csv')
print('DF SHAPE')
print(df.shape)

print('DF DETAILS:')
print(df.describe())

print('\nDF INFO:')
print(df.info())

print('\nTotal null:')
print(df.isnull().sum())

print('\nDuplicate:')
print(df.duplicated())
print(df.duplicated().sum())

