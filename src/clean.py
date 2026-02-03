import pandas as pd

def extract_numeric(df):
    df['max_power'] = df['max_power'].str.extract(r'([\d\.]+)\s*bhp')       #()=>BAT GIA TRI, \d =>0-9, + =>NHIEU SO
    df['engine'] = df['engine'].str.extract(r'(\d+)\s*CC')              #\s =>KHOANG TRANG, * => CO HOAC KHONG
    df[['mileage','mileage_unit']] = df['mileage'].str.extract(r'([\d\.]+)\s*(kmpl|km/kg)')             #==> CHI BAT SO
    return df

def change_types(df):
    columns = ['selling_price','max_power','engine','mileage','year','seats','km_driven']
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def handle_missing(df):
    df['torque'] = df['torque'].fillna('unknown')
    df['seats'] = df['seats'].fillna(df['seats'].mode()[0])

    important_columns = ['mileage', 'engine', 'max_power']
    df = df[df[important_columns].isnull().sum(axis = 1) < 3]           #CONG NULL THEO HANG

    columns = ['mileage','engine','max_power']
    for column in columns:
        df.loc[:, column] = df[column].fillna(df[column].median())  # DIEN O NULL BANG TRUNG VI
    return df

def handle_duplicate(df):
    df = df.drop_duplicates(keep = 'first')
    return df

def valid_value(df):
    columns = ['mileage', 'engine', 'max_power','seats']
    for column in columns:
        df = df[df[column] > 0]
    return df

def main():
    df = pd.read_csv('../data/raw/Car details v3.csv')
    df = extract_numeric(df)
    df =change_types(df)
    df = handle_missing(df)
    df = handle_duplicate(df)
    df = valid_value(df)
    df.to_csv('../data/processed/clean_Car_details.csv', index = False)
if __name__ == '__main__':
    main()