import pandas as pd
df = pd.read_table(r"wr88125.txt", sep = ';',
                   names = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall'])

# Выводим первые 5 наблюдений
print(df.head(), '\n')


# Удаляем лишние проблемы с помощью replace
df['min_t'] = df['min_t'].str.replace(' ', '')
df['average_t'] = df['average_t'].str.replace(' ', '')
df['max_t'] = df['max_t'].str.replace(' ', '')
df['rainfall'] = df['rainfall'].str.replace(' ', '')

# Преобразование пробелов к числовому типу
df = df.apply(pd.to_numeric)
print(df.info(), '\n')

# Удаляем столбец 'index'
del df['index']

# Создаем пустую серию, индексами в которой являются значения от 1960 до 2020
s = pd.Series(index=range(1960,2021), dtype=float)
for i in range(1960, 2021):
    s[i] = df[df['year'] == i].isnull().sum().sum()
print(s.idxmax(), '\n')

df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
print(df.head(), '\n')


df['range_t'] = df['max_t']-df['min_t']

s_1 = df.groupby('year')['average_t'].mean() # Вычисляем среднегодовю температуру для каждого года и записываем в серию

print(s_1.head(), '\n')
print(s_1.idxmax(), '\n')
print(s_1[2020], '\n')
print(s_1.idxmin(), '\n')

print(df[df['average_t'] < -30], '\n')

print(df[(df['average_t'] > 27) & (df['rainfall'] == 0)])