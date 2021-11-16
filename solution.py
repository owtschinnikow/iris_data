import pandas
from docutils.parsers.rst.directives.misc import Title

title = 'Iris Flower Summary \n All Flowers'

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

metric_1_list = [[0]*4 for i in range(6)]
metric_2_list = [[0]*4 for i in range(6)]
metric_3_list = [[0]*4 for i in range(6)]
metric_4_list = [[0]*4 for i in range(6)]


dataframe = pandas.read_csv('iris_data.csv', header=None)
print(dataframe)

for i in range(0, number_of_flowers):
    metric_1_list[0][0] += dataframe[0][i]  # сумма для среднего
    if i == 0:
        metric_1_list[1][0] = dataframe[0][i]
    if metric_1_list[1][0] >= dataframe[0][i]:  # вычисление минимума
        metric_1_list[1][0] = dataframe[0][i]
    if metric_1_list[2][0] <= dataframe[0][i]:  # вычисление максимума
        metric_1_list[2][0] = dataframe[0][i]

metric_1_list[0][0] = metric_1_list[0][0]/number_of_flowers  # вычисление среднего

# dataframe.median(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)

dataframe_1 = dataframe[0:50]
print('dataframe_1')
print(dataframe_1)
print(metric_1_list)


# dataframe.to_csv('iris-flowers.txt')

# filename = w'iris-flowers.txt'
#
# pandas.read_table(filename,sep='\s+', engine='python')

