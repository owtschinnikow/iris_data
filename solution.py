import pandas

#Базовые названия
title = 'Iris Flower Summary'
flowor_1 = 'Iris-setosa'
flowor_2 = 'Iris-versicolor'
flowor_3 = 'Iris-virginica'
total = 'Total'
number_of_flowers = 50

#Формирование массива
metric_1_list = [['']*5 for i in range(15+11+1)]

#Заполнение массива полями
metric_1_list[0][2] = title
metric_1_list[1][1] = flowor_1
metric_1_list[1][2] = flowor_2
metric_1_list[1][3] = flowor_3
metric_1_list[1][4] = total

for i in range(1, 4):
    metric_1_list[2][i] = f' n = {number_of_flowers}'
    metric_1_list[4][i] = f'{number_of_flowers}'

metric_1_list[2][4] = f' n = {number_of_flowers*3}'
metric_1_list[4][4] = f'{number_of_flowers*3}'

for dy in [0, 12]:
    if dy == 0:
        metric_1_list[3 + dy][0] = 'SEPAL LENGTH [CM]'#'Sepal Lenght [CM]'
        metric_1_list[10+ dy][0] = 'SEPAL LENGTH (%) '  # 'SEPAL LENGTH (%) '
    elif dy == 12:
        metric_1_list[3 + dy][0] = 'SEPAL WIDTH [CM]'#'Sepal Lenght [CM]'
        metric_1_list[10+ dy][0] = 'SEPAL WIDTH (%)'  # 'SEPAL LENGTH (%) '
    metric_1_list[4 + dy][0] = 'N'
    metric_1_list[5 + dy][0] = 'MEAN'
    metric_1_list[6 + dy][0] = 'MIN'
    metric_1_list[7 + dy][0] = 'MAX '
    metric_1_list[8 + dy][0] = 'MEDIAN'
    metric_1_list[9 + dy][0] = 'STANDARD DEVIATION'

metric_1_list[11][0] = '< 5'
metric_1_list[12][0] = '>=5 AND <6'
metric_1_list[13][0] = '>=6 AND <7'
metric_1_list[14][0] = '>= 7'

metric_1_list[23][0] = '< 3'
metric_1_list[24][0] = '>=3 AND <3.5'
metric_1_list[25][0] = '>=3.5 AND <4'
metric_1_list[26][0] = '>= 4'  # Не было в задании, добавлено для красоты таблицы.

# Подгрузка данных из файла.
dataframe = pandas.read_csv('iris_data.csv', header=None)


# ПРЕДПОЛОЖИТЕЛЬНО более быстрый расчёт среднего, минимума, максимума по сравнению со стандартными методами
for dx, dy in [(0,0), (1,50), (2,100)]:
    for i in range(0, number_of_flowers):
        # вычисление среднего
        if i == 0:
            metric_1_list[5][1 + dx] = 0
        metric_1_list[5][1 + dx] += dataframe[0][i + dy]

        # вычисление минимума
        if i == 0:
            metric_1_list[6][1 + dx] = dataframe[0][i + dy]
        if metric_1_list[6][1 + dx] >= dataframe[0][i + dy]:
            metric_1_list[6][1 + dx] = dataframe[0][i + dy]

        # вычисление максимума
        if i == 0:
            metric_1_list[7][1 + dx] = 0
        if metric_1_list[7][1 + dx] <= dataframe[0][i + dy]:
            metric_1_list[7][1 + dx] = dataframe[0][i + dy]

    metric_1_list[5][1 + dx] = "{:.2f}".format(metric_1_list[5][1 + dx]/number_of_flowers)  # вычисление среднего
    metric_1_list[6][1 + dx] = "{:.2f}".format(metric_1_list[6][1 + dx])  # вычисление минимума
    metric_1_list[7][1 + dx] = "{:.2f}".format(metric_1_list[7][1 + dx])

# dataframe.median(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)

# Использование стандартных функций .describe() .loc['mean'][0] и тд...
# Расчёт для каждого вида 'count', 'mean', 'min', 'max', 'std' median
for dx, df in [(0, 0), (1, 50), (2, 100)]:
    metric_1_list[16][1+dx] = "{:.0f}".format(dataframe[0+df:50+df].describe().loc['count'][1])
    metric_1_list[17][1+dx] = "{:.2f}".format(dataframe[0+df:50+df].describe().loc['mean'][1])
    metric_1_list[18][1+dx] = "{:.2f}".format(dataframe[0+df:50+df].describe().loc['min'][1])
    metric_1_list[19][1+dx] = "{:.2f}".format(dataframe[0+df:50+df].describe().loc['max'][1])
    metric_1_list[20][1+dx] = "{:.2f}".format(dataframe[0+df:50+df].median()[1])
    metric_1_list[21][1+dx] = "{:.2f}".format(dataframe[0+df:50+df].describe().loc['std'][1])

    metric_1_list[8][1 + dx] = "{:.2f}".format(dataframe[0 + df:50 + df].median()[0])
    metric_1_list[9][1 + dx] = "{:.2f}".format(dataframe[0 + df:50 + df].describe().loc['std'][0])

# Расчёт для общего количества 'count', 'mean', 'min', 'max', 'std' median
for dx in [0, 12]:
    metric_1_list[4 + dx][4] = "{:.0f}".format(dataframe[0:150].describe().loc['count'][0])
    metric_1_list[5 + dx][4] = "{:.2f}".format(dataframe[0:150].describe().loc['mean'][0])
    metric_1_list[6 + dx][4] = "{:.2f}".format(dataframe[0:150].describe().loc['min'][0])
    metric_1_list[7 + dx][4] = "{:.2f}".format(dataframe[0:150].describe().loc['max'][0])
    metric_1_list[8 + dx][4] = "{:.2f}".format(dataframe[0:150].median()[0])
    metric_1_list[9 + dx][4] = "{:.2f}".format(dataframe[0:150].describe().loc['std'][0])

#Расчёт второй секции для S/L
for dx, dy in [(0,0), (1, 50), (2, 100)]:
    df_1 = dataframe[0][0+dy:50+dy]
    quantity_less_5 = (df_1 < 5).sum()
    percent_less_5 = quantity_less_5 / number_of_flowers * 100
    metric_1_list[11][1+dx] = str(quantity_less_5) + ' (' + str(percent_less_5) + ')'

    quantity_less_5_6 = ((5 <= df_1) * ( df_1 < 6) ).sum()
    percent_less_5_6= quantity_less_5_6 / number_of_flowers * 100
    metric_1_list[12][1+dx] = str(quantity_less_5_6) + ' (' + str(percent_less_5_6) + ')'

    quantity_less_6_7 = ((6 <= df_1) * ( df_1 < 7) ).sum()
    percent_less_6_7= quantity_less_6_7 / number_of_flowers * 100
    metric_1_list[13][1+dx] = str(quantity_less_6_7) + ' (' + str(percent_less_6_7) + ')'

    quantity_less_7 =  ( 7 <= df_1).sum()
    percent_less_7= quantity_less_7 / number_of_flowers * 100
    metric_1_list[14][1+dx] = str(quantity_less_7) + ' (' + str(percent_less_7) + ')'

#Расчёт второй секции для S/L Total
for dx, dy in [(3, 0)]:
    df_1 = dataframe[0][0+dy:150+dy]
    quantity_less_5 = (df_1 < 5).sum()
    percent_less_5 = "{:.1f}".format(quantity_less_5 / (number_of_flowers*3) * 100)
    metric_1_list[11][1+dx] = str(quantity_less_5) + ' (' + str(percent_less_5) + ')'

    quantity_less_5_6 = ((5 <= df_1) * ( df_1 < 6) ).sum()
    percent_less_5_6= "{:.1f}".format(quantity_less_5_6 / (number_of_flowers*3) * 100)
    metric_1_list[12][1+dx] = str(quantity_less_5_6) + ' (' + str(percent_less_5_6) + ')'

    quantity_less_6_7 = ((6 <= df_1) * ( df_1 < 7) ).sum()
    percent_less_6_7= "{:.1f}".format(quantity_less_6_7 / (number_of_flowers*3) * 100)
    metric_1_list[13][1+dx] = str(quantity_less_6_7) + ' (' + str(percent_less_6_7) + ')'

    quantity_less_7 =  ( 7 <= df_1).sum()
    percent_less_7= "{:.1f}".format(quantity_less_7 / (number_of_flowers*3) * 100)
    metric_1_list[14][1+dx] = (str(quantity_less_7) + ' (' + str(percent_less_7) + ')')

#Расчёт второй секции для S/W
for dx, dy in [(0,0), (1, 50), (2, 100)]:
    df_1 = dataframe[1][0+dy:50+dy]
    quantity_less_3 = (df_1 < 3).sum()
    percent_less_3 = quantity_less_3 / number_of_flowers * 100
    metric_1_list[23][1+dx] = str(quantity_less_3) + ' (' + str(percent_less_3) + ')'

    quantity_less_3_35 = ((3 <= df_1) * ( df_1 < 3.5) ).sum()
    percent_less_3_35= quantity_less_3_35 / number_of_flowers * 100
    metric_1_list[24][1+dx] = str(quantity_less_3_35) + ' (' + str(percent_less_3_35) + ')'

    quantity_less_35_4 = ((3.5 <= df_1) * ( df_1 < 4) ).sum()
    percent_less_35_4= quantity_less_35_4 / number_of_flowers * 100
    metric_1_list[25][1+dx] = str(quantity_less_35_4) + ' (' + str(percent_less_35_4) + ')'

    quantity_less_4 = ((4 <= df_1) ).sum()
    percent_less_4= quantity_less_4 / number_of_flowers * 100
    metric_1_list[26][1+dx] = str(quantity_less_4) + ' (' + str(percent_less_4) + ')'


#Расчёт второй секции для S/W Total
for dx, dy in [(3, 0)]:
    df_1 = dataframe[1][0+dy:150+dy]
    quantity_less_3 = (df_1 < 3).sum()
    percent_less_3 = "{:.1f}".format(quantity_less_3 / (number_of_flowers*3) * 100)
    metric_1_list[23][1+dx] = str(quantity_less_3) + ' (' + str(percent_less_3) + ')'

    quantity_less_3_35 = ((3 <= df_1) * ( df_1 < 3.5) ).sum()
    percent_less_3_35= "{:.1f}".format(quantity_less_3_35 / (number_of_flowers*3) * 100)
    metric_1_list[24][1+dx] = str(quantity_less_3_35) + ' (' + str(percent_less_3_35) + ')'

    quantity_less_35_4 = ((3.5 <= df_1) * ( df_1 < 4) ).sum()
    percent_less_35_4= "{:.1f}".format(quantity_less_35_4 / (number_of_flowers*3) * 100)
    metric_1_list[25][1+dx] = str(quantity_less_35_4) + ' (' + str(percent_less_35_4) + ')'

    quantity_less_4 = ((4 <= df_1) ).sum()
    percent_less_4= "{:.1f}".format(quantity_less_4 / (number_of_flowers*3) * 100)
    metric_1_list[26][1+dx] = str(quantity_less_4) + ' (' + str(percent_less_4) + ')'

# Генерация массива из списка.
df = pandas.DataFrame(metric_1_list)

# Выгрузка в файл.
df.to_latex('iris-flowers.txt', index = False, header = False)


