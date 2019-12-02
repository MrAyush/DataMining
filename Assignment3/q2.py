from statistics import mean, median

data_set_raw = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25,
                25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
split_data = [data_set_raw[x:x + 3] for x in range(0, len(data_set_raw), 3)]

print('Smoothing by bin means')
for k, data in enumerate(split_data):
    print(f'bin {k}: {[int(mean(data) / 3)] * 3}')

print('')

print('Smoothing by bin medians')
for k, data in enumerate(split_data):
    print(f'bin {k}: {[int(median(data))] * 3}')

print('')

print('Smoothing by bin boundaries')
for k, data in enumerate(split_data):
    l = []
    for x in data:
        if x - data[0] < data[-1] - x:
            l.append(data[0])
        else:
            l.append(data[-1])
    print(f'bin {k}: {l}')
