# url for iris data set = 'https://tableconvert.com/?output=csv&data=https://gist.githubusercontent.com/curran
#                               /a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv'

import pandas as pd


def min_max_scaling(data_set):
    return (data_set - data_set.min()) / (data_set.max() - data_set.min())


def z_score_scaling(data_set):
    return (data_set - data_set.mean()) / data_set.std(ddof=0)


def decimal_scaling(data_set):
    s = len(str(data_set.max()))
    return data_set / (10 ** s)


dataframe = pd.DataFrame(pd.read_csv('./iris.csv'))

data_columns = [x for x in dataframe.columns if x != 'species']
dataframe_min_max = pd.DataFrame()
for col in data_columns:
    dataframe_min_max[col] = min_max_scaling(dataframe[col])

dataframe_z_score = pd.DataFrame()
for col in data_columns:
    dataframe_z_score[col] = z_score_scaling(dataframe[col])
dataframe_z_score['species'] = dataframe['species']

dataframe_decimal = pd.DataFrame()
for col in data_columns:
    dataframe_decimal[col] = decimal_scaling(dataframe[col])
dataframe_decimal['species'] = dataframe['species']

print(f'Top 5 rows after min max scaling:\n{dataframe_min_max.head()}')
print(f'Top 5 rows after z-score scaling:\n{dataframe_z_score.head()}')
print(f'Top 5 rows after decimal scaling:\n{dataframe_decimal.head()}')
