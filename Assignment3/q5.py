import pandas as pd


def min_max_scaling(data_set, value):
    return (value - data_set.min()) / (data_set.max() - data_set.min())


def z_score_scaling(data_set, value):
    return (value - data_set.mean()) / data_set.std(ddof=0)


def decimal_scaling(data_set, value):
    s = len(str(data_set.max()))
    return value / (10 ** s)


data_set_raw = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25,
                25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
data_set = pd.Series(data_set_raw)

print(f'Min Max Scaling of 35: {min_max_scaling(data_set, 35):.4f}')
print(f'Z-score Scaling of 35: {z_score_scaling(data_set, 35):.4f}')
print(f'Decimal Scaling of 35: {decimal_scaling(data_set, 35):.4f}')
