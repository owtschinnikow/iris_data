import statistics
import numpy
import pandas
import csv

flowor_1 = 'Iris-setosa'
flowor_2 = 'Iris-versicolor'
flowor_3 = 'Iris-virginica'

number_of_flowers = 50

metric_1 = 'SEPAL LENGTH'
metric_2 = 'SEPAL WIDTH'
metric_3 = 'PETAL LENGTH'
metric_4 = 'PETAL WIDTH'

dataframe = pandas.read_csv('iris_data.csv', header=None )
# print(dataframe)

print(dataframe[2][2]+dataframe[2][3])

print(dataframe[4][2])

if dataframe[4][2] == flowor_1:
    print(flowor_1, 222222)
