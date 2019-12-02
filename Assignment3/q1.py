import matplotlib.pyplot as plot
import pandas

data_set_raw = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25,
                25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
data_set = pandas.Series(data_set_raw)
print(f'i.   Mean: {data_set.mean():.2f}, Median: {data_set.median()}')
print(f'ii.  Mode(s): ', end="")
[print(x, end=", ") for x in data_set.mode()]
print('\b\b')
print(f'iii. Mid Range {(data_set.min() + data_set.max()) / 2}')
print(f'iv.  First Quartile: {int(data_set.quantile(0.25))}, Third Quartile: {int(data_set.quantile(0.75))}')

# v. box plot is saved as Figure_1.png

plot.boxplot(data_set)
plot.show()

# vi. Q-Q plot saved as Figure_2.png

plot.scatter(data_set, range(0, len(data_set)))
plot.plot(data_set, data_set * 3/7, "k--", linewidth=2)
plot.show()
