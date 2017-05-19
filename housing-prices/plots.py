import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import model as mdl


def create_date_cols(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    sold_date = df['date']
    df['day'] = sold_date.apply(lambda x: x.day) + 1
    df['month'] = sold_date.apply(lambda x: x.month)
    df['count'] = 1
    return df


def plot_daily_sales(df, n):
    month = df[df['month'] == n]
    if len(month) != 0:
        month_count = month.groupby('date').count()['count']
        month_count.plot(marker='o', markersize=7, alpha=.4, rot=90)


def plot_size_change(df):
    df['lot_size_change'] = df['sqft_living15'] - df['sqft_living']
    df['house_size_change'] = df['sqft_lot15'] - df['sqft_lot']
    plt.subplot(2, 2, 1)
    plt.scatter(df['lot_size_change'], df['price'])
    plt.xlabel('Lot Size Change')
    plt.ylabel('price')
    plt.subplot(2, 2, 2)
    plt.scatter(df['house_size_change'], df['price'])
    plt.xlabel('House Size Change')
    plt.ylabel('price')


def plot_residuals(df, columns):
    model = mdl.train_model(df.iloc[0:10000], dropped_columns=columns)
    residuals = model.outlier_test()['student_resid']
    plt.plot(model.fittedvalues, residuals, 'o')
    plt.axhline(0, color='r')
    plt.xlabel('predicted response')
    plt.ylabel('studentized residuals')
    plt.show()
    return model.fittedvalues, residuals

if __name__ == '__main__':
    housing_data = create_date_cols('data/kc_house_data.csv')
    # for i in range(0, 13):
    #     plot_monthly_sales(housing_data, i)
    # plt.xlabel('Month')
    # plt.ylabel('Number of Sales')
    # plt.show()
    predicted, residuals = plot_residuals(housing_data, ['price', 'yr_renovated', 'zipcode',
                                                         'lat', 'long', 'id', 'date', 'sqft_living15',
                                                         'sqft_lot15', 'sqft_above', 'sqft_basement', 'floors', 'sqft_living', 'sqft_lot'])
