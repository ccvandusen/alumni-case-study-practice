import pandas as pd
import numpy as np
import statsmodels.api as sm


def import_data(filename):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df.date)
    return df


def dummify_variables(df, var_names):
    '''
    INPUT: pandas df from import_data fxn
           list of column names to dummify
    OUTPUT: pandas df with dummified variables from list
    '''
    if 'grade' in var_names:
        grade_dummies = pd.get_dummies(
            pd.cut(df['grade'], bins=[0, 4, 7, 10, 13]))
        grade_dummies.columns = ['low_grade',
                                 'mid_grade', 'high_grade', 'higher_grade']

    return df.join(grade_dummies).drop(['grade', 'low_grade'], axis=1)


def train_model(data, print_summary=False):
    y = np.log(data['price'])
    X = data.drop(['price', 'yr_renovated', 'zipcode',
                   'lat', 'long', 'id', 'date', 'sqft_living15',
                   'sqft_lot15', 'sqft_above', 'sqft_basement', 'floors'], axis=1)
    model = sm.OLS(list(y), X)
    result = model.fit()
    if print_summary:
        print result.summary()
    else:
        return result


if __name__ == '__main__':
    df = import_data('data/kc_house_data.csv')
    df = dummify_variables(df, ['grade'])
    model = train_model(df)
