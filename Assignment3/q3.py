import pandas as pd
import matplotlib.pyplot as plot

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

frame = pd.DataFrame(zip(age, fat), columns=['age', 'fat'])
print(f'(age, %fat)Means: ({frame["age"].mean():.2f}, {frame["fat"].mean():.2f})')
print(f'(age, %fat)Median: ({frame["age"].median():.2f}, {frame["fat"].median():.2f})')
print(f'(age, %fat)Standard Deviation: ({frame["age"].std():.2f}, {frame["fat"].std():.2f})')
# Figure_3
plot.boxplot(frame)
plot.xlabel('% Fat')
plot.ylabel('Age')
plot.show()
# Figure_4
plot.scatter(frame['age'], frame['fat'])
plot.xlabel('% Fat')
plot.ylabel('Age')
plot.show()
# Figure_5
plot.scatter(frame['age'], frame['fat'])
plot.plot(frame['age'], frame['age'] * 4/7)
plot.xlabel('% Fat')
plot.ylabel('Age')
plot.show()

print('Normalization of Data using z-score')
for col in list(frame.columns):
    frame[col] = (frame[col] - frame[col].mean())/(frame[col].std(ddof=0))
print(frame)
print('Correlation of variables:')
print(frame.corr())
