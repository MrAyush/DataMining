data_set_raw = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]


def split_data_equal_width(data_set_raw):
    split_data = []
    w = (max(data_set_raw) - min(data_set_raw)) // 3
    i = 1
    a = min(data_set_raw)
    interval = min(data_set_raw) + i * w
    for _ in range(1, 4):
        split_data.append([x for x in data_set_raw if a < x <= interval])
        a = interval
        i = i + 1
        interval = min(data_set_raw) + (i * w)
    return split_data


def split_data_cluster(data_set_raw):
    l = []
    for i in range(1, len(data_set_raw)):
        l.append(data_set_raw[i] - data_set_raw[i - 1])
    y = []
    y.append(l.index(max(l)))
    l.remove(max(l))
    y.append(l.index(max(l)))
    y.sort()
    split_data_set_cluster = [data_set_raw[0:y[0] + 1], data_set_raw[y[0] + 1:y[1] + 1], data_set_raw[y[1] + 1:]]
    return split_data_set_cluster


split_data_set = [data_set_raw[x:x + 4] for x in range(0, len(data_set_raw), 4)]
print(f'i.   Equal-frequency(equi-depth) partitioning {split_data_set}')
print(f'ii.  Equal-width partitioning {split_data_equal_width(data_set_raw)}')
print(f'iii. Clustering partitioning {split_data_cluster(data_set_raw)}')