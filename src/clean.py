import pandas as pd

def extract_numeric(df):
    df['max_power'] = df['max_power'].str.extract(r'(\d+)\s*bhp')       #()=>BAT GIA TRI, \d =>0-9, + =>NHIEU SO
    df['engine'] = df['engine'].str.extract(r'(\d+)\s*CC')              #\s =>KHOANG TRANG, * => CO HOAC KHONG
    df['mileage'] = df['mileage'].str.extract(r'(\d+)\s*kmpl|km/kg')
    #df['mileage'] = df['mileage'].str.extract(r'([\d\.]+)') ==> CHI BAT SO

def handle_missing(df):
    df['torque'] = df['torque'].fillna('unknown')

    important_columns = ['mileage', 'engine', 'max_power', 'torque']
    df = df[df[important_columns].isnull().sum(axis = 1) < 3]           #CONG NULL THEO HANG

    for column in ['mileage', 'engine', 'max_power']:
        df[column] = df[column].fillna(df[column].median())             #DIEN O NULL BANG TRUNG VI

    df['seats'] = df['seats'].fillna(df['seat'].mode()[0])

def main():
    df = pd.read_csv('../data/raw/Car details v3.csv')
    extract_numeric(df)
if __name__ == '__main__':
    main()