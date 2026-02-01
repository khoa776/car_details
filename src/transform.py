import numpy as np
import pandas as pd

def car_age(df):
    df['car_age'] = 2026 - df['year']

    bins = [0,3,6,10,15,30]
    labels = ['0–3 năm', '4–6 năm', '7–10 năm', '11–15 năm', '>15 năm']
    df['car_age_group'] = pd.cut(df['car_age'], bins = bins, labels = labels)
    return df

def data_group(df):
    df['km_group'] = pd.qcut(df['km_driven'],q=5,labels=['Rất thấp', 'Thấp', 'Trung bình', 'Cao', 'Rất cao'])
    df['engine_group'] = pd.cut(df['engine'],bins = [0,1000,1500,2000,3000,5000],
                              labels = ['Duoi 1000 CC', '1000-1500 CC', '1500-2000 CC', '2000-3000 CC', 'Tren 3000 CC' ])
def total_selling_price_by_fuel(df):
    selling_by_fuel = (df.groupby(['fuel','mileage_unit'],as_index=False)
                       .agg(
                            total_selling_price = ('selling_price', 'sum'),
                            total_sale =  ('fuel', 'count')
                            )
                       )
    return selling_by_fuel


def main():
    df = pd.read_csv('../data/processed/clean_Car_details.csv')
    df = car_age(df)
    selling_by_fuel = total_selling_price_by_fuel(df)



    selling_by_fuel = selling_by_fuel.sort_values('total_selling_price',ascending=False)
    print(selling_by_fuel)
    import matplotlib.pyplot as plt

    cols = ['mileage', 'engine', 'max_power']

if __name__ == '__main__':
    main()