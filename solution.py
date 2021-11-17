import pandas
from docutils.parsers.rst.directives.misc import Title

title = 'Iris Flower Summary'

# columns
flowor_1 = 'Iris-setosa'
flowor_2 = 'Iris-versicolor'
flowor_3 = 'Iris-virginica'
total = 'Total'

number_of_flowers = 50

metric_1_name = 'SEPAL LENGTH'
metric_2_name = 'SEPAL WIDTH'
metric_3_name = 'PETAL LENGTH'
metric_4_name = 'PETAL WIDTH'

metric_1_list = [['']*5 for i in range(3+3+7+5+7+5)]
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

metric_1_list[3][0] = 'S/L [CM]'#'Sepal Lenght [CM]'
metric_1_list[4][0] = 'N'
metric_1_list[5][0] = 'MEAN'
metric_1_list[6][0] = 'MIN'
metric_1_list[7][0] = 'MAX '
metric_1_list[8][0] = 'MEDIAN'
metric_1_list[9][0] = 'S/D'#'STANDARD DEVIATION'
metric_1_list[10][0] = 'S/L (%) '#'SEPAL LENGTH (%) '
metric_1_list[11][0] = '< 5'
metric_1_list[12][0] = '>=5 AND <6'
metric_1_list[13][0] = '>=6 AND <7'
metric_1_list[14][0] = '>= 7'



dataframe = pandas.read_csv('iris_data.csv', header=None)


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

print(metric_1_list)

df = pandas.DataFrame(metric_1_list)
print(df)

df.to_csv('iris-flowers.txt', sep='\t', index = False, header = False )


