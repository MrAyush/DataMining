import pandas as pd


def min_max_scaling(data_set):
    return (data_set - data_set.min()) / (data_set.max() - data_set.min())


def z_score_scaling(data_set):
    return (data_set - data_set.mean()) / data_set.std(ddof=0)


def z_score_abs_mean_scaling(data_set):
    return (data_set - data_set.mean()) / data_set.mad()


def decimal_scaling(data_set):
    s = len(str(data_set.max()))
    return data_set / (10 ** s)


data_set_raw = [200, 300, 400, 600, 1000]
data_set = pd.Series(data_set_raw)
min_max_data_set = list(min_max_scaling(data_set))
print(f'After Min-Max Normalization: {min_max_data_set}')
z_score_data_set = list(z_score_scaling(data_set))
print(f'After Z-score Normalization: {z_score_data_set}')
z_score_abs_mean_data_set = list(z_score_abs_mean_scaling(data_set))
print(f'After Z-score abs mean Normalization: {z_score_abs_mean_data_set}')
decimal_data_set = list(decimal_scaling(data_set))
print(f'After Decimal Normalization: {decimal_data_set}')
