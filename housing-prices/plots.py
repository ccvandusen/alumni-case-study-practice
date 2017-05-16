import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_date_cols(filepath):
    df = pd.read_csv(filepath, parse_dates='date')
    sold_date = df['date']
    df['day'] = sold_date.apply(lambda x: x.day) + 1
    df['month'] = sold_date.apply(lambda x: x.month)
    df['count'] = 1
    return df


def plot_monthly_sales(df, n):
    month = df[df['year'] == n]
    month_count = month.groupby('date').count()['count']
    year_count.plot(marker='o', markersize=7, alpha=.4, rot=90)


if __name__ == '__main__':
    housing_data = create_date_cols('data/kc_house_data.csv')
    for i in range(0, 13):
        plot_monthly_sales(housing_data)
