import pandas as pd
import numpy as np
import statsmodels.api as sm


def import_data(filename):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df.date)
    return df


def print_summary(data):
    y = data['price']
    X = data.drop(['price', 'yr_renovated', 'zipcode',
                   'lat', 'long', 'id', 'date'], axis=1)
    model = sm.OLS(list(y), X)
    result = model.fit()
    print result.summary()

if __name__ == '__main__':
    df = import_data('data/kc_house_data.csv')
    print_summary(df)
