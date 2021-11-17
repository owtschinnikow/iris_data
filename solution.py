import pandas
from docutils.parsers.rst.directives.misc import Title

title = 'Iris Flower Summary'


flowor_1 = 'Iris-setosa'
flowor_2 = 'Iris-versicolor'
flowor_3 = 'Iris-virginica'
total = 'Total'

number_of_flowers = 50

metric_1_name = 'SEPAL LENGTH'
metric_2_name = 'SEPAL WIDTH'
metric_3_name = 'PETAL LENGTH'
metric_4_name = 'PETAL WIDTH'

metric_1_list = [['']*5 for i in range(15+11)]
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
        metric_1_list[3 + dy][0] = 'S/L [CM]'#'Sepal Lenght [CM]'
        metric_1_list[10+ dy][0] = 'S/L (%) '  # 'SEPAL LENGTH (%) '
    elif dy == 12:
        metric_1_list[3 + dy][0] = 'S/W [CM]'#'Sepal Lenght [CM]'
        metric_1_list[10+ dy][0] = 'S/W (%)'  # 'SEPAL LENGTH (%) '
    metric_1_list[4 + dy][0] = 'N'
    metric_1_list[5 + dy][0] = 'MEAN'
    metric_1_list[6 + dy][0] = 'MIN'
    metric_1_list[7 + dy][0] = 'MAX '
    metric_1_list[8 + dy][0] = 'MEDIAN'
    metric_1_list[9 + dy][0] = 'S/D'#'STANDARD DEVIATION'

metric_1_list[11][0] = '< 5'
metric_1_list[12][0] = '>=5 AND <6'
metric_1_list[13][0] = '>=6 AND <7'
metric_1_list[14][0] = '>= 7'

metric_1_list[23][0] = '< 3'
metric_1_list[24][0] = '>=3 AND <3.5'
metric_1_list[25][0] = '>=3.5 AND <4'

dataframe = pandas.read_csv('iris_data.csv', header=None)


# ПРЕДПОЛОЖИТЕЛЬНО более быстрый расчёт по сравнению со стандартным методом
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

    metric_1_list[5][1 + dx] = "{:.1f}".format(metric_1_list[5][1 + dx]/number_of_flowers)  # вычисление среднего

# dataframe.median(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)

# Использование функции .describe() .loc['mean'][0]
# Расчёт для каждого вида 'count', 'mean', 'min', 'max', 'std' median
for dx, df in [(0, 0), (1, 50), (2, 100)]:
    # df_1 = dataframe[0+df:50+df].describe()
    # print(df_1)
    metric_1_list[16][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].describe().loc['count'][1])
    metric_1_list[17][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].describe().loc['mean'][1])
    metric_1_list[18][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].describe().loc['min'][1])
    metric_1_list[19][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].describe().loc['max'][1])
    metric_1_list[20][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].median()[1])
    metric_1_list[21][1+dx] = "{:.1f}".format(dataframe[0+df:50+df].describe().loc['std'][1])

    metric_1_list[8][1 + dx] = "{:.1f}".format(dataframe[0 + df:50 + df].median()[0])
    metric_1_list[9][1 + dx] = "{:.1f}".format(dataframe[0 + df:50 + df].describe().loc['std'][0])

# Расчёт для общего количества 'count', 'mean', 'min', 'max', 'std' median
for dx in [0, 12]:
    # df_1 = dataframe[0:150].describe()
    # print(df_1)
    metric_1_list[4 + dx][4] = "{:.1f}".format(dataframe[0:150].describe().loc['count'][0])
    metric_1_list[5 + dx][4] = "{:.1f}".format(dataframe[0:150].describe().loc['mean'][0])
    metric_1_list[6 + dx][4] = "{:.1f}".format(dataframe[0:150].describe().loc['min'][0])
    metric_1_list[7 + dx][4] = "{:.1f}".format(dataframe[0:150].describe().loc['max'][0])
    metric_1_list[8 + dx][4] = "{:.1f}".format(dataframe[0:150].median()[0])
    metric_1_list[9 + dx][4] = "{:.1f}".format(dataframe[0:150].describe().loc['std'][0])



# for i in range(2):
#     metric_1_list[8][1+i] = dataframe[0:50].median()[i]



df = pandas.DataFrame(metric_1_list)
print(df)

df.to_csv('iris-flowers.txt', sep='\t', index = False, header = False )


