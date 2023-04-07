import statistics

import pandas as pd
from numpy import mean

space = "_" * 50

url = 'Pesquisa_sala.xlsx'

df = pd.read_excel('Pesquisa_sala.xlsx')

# print(df.columns)

categories = []
numbers = []

# append adds an element to the list
# obejct is the string data type
for column in df.columns:
    if df[column].dtype == 'object':
        categories.append(column)
    else:
        numbers.append(column)


print('\nCategorical variables:', categories)
print('Numerical variables:', numbers)

print(space)

# average counts only numerical variables
# the average
mediaBeauty = df['Beleza'].mean()
print('\nAverage beauty is:', mediaBeauty)
print(space)

averageAge = df['Idade'].mean()
print('Average age is:', averageAge)
print(space)

# b) median
medianBeauty = df['Beleza'].median()
print('\nMedian beauty is:', medianBeauty)

medianAge = df['Idade'].median()
print('Median age is:', medianAge)
print(space)

# c) fashion
fashionName = statistics.mode(df['Nome'])
print('Fashion of the name is:', fashionName)

fashionCity = statistics.mode(df['Cidade '])
print('City Fashion is:', fashionCity)

fashionBeauty = statistics.mode(df['Beleza'])
print('\nBeauty fashion is:', fashionBeauty)

fashionAge = statistics.mode(df['Idade'])
print('Age fashion is:', fashionAge)
print(space)

# standard deviation counts numeric variables only
# d) standard deviation
DVPB = statistics.pstdev(df['Beleza'])
print('\nThe standard deviation of Beauty is:', DVPB)

DVPI = statistics.pstdev(df['Idade'])
print('The standard deviation of Age is:', DVPI)
print(space)


# e) total amplitude
amplitudeAge = df['Idade'].max() - df['Idade'].min()
print('\nTotal range of age is:', amplitudeAge)

amplitudeBeauty = df['Beleza'].max() - df['Beleza'].min()
print('Total amplitude of beauty is:', amplitudeBeauty)
print(space)

# f) coefficient of variation
CVI = statistics.pstdev(df['Idade'])/mean(df['Idade'])
print('\nCoefficient of variation of age is:', CVI)

CVB = statistics.pstdev(df['Beleza'])/mean(df['Beleza'])
print('Coefficient of variation of beauty is:', CVB)
print(space)

tempoAposentadoria = df['Time for retirement'] = 70 - df['Idade']
print(df.head(20))

print(space)

# sorting by city
cityGroup = df.groupby('Cidade ')
# print(cityGroup)

# checking the beauty average of each city
# ascending=flase sorts from highest to lowest
mediaCityBeauty = cityGroup['Beleza'].mean().sort_values(ascending=False)

# index[0] serves to get the name of the city
print('\na) Which city has the highest average beauty?',
      mediaCityBeauty.index[0])
# print(mediaCityBeauty)

# ascending=True ordena do menor para o maior
averageCityAge = cityGroup['Idade'].mean().sort_values(ascending=True)
print('b) Which city has the lowest mean age?',
      averageCityAge.index[0])
# print(averageCityAge)
print(space)

# Group data by beauty
beautygroup = df.groupby('Beleza')

# Calculate age standard deviation for each beauty group
# Example code: DataFrame.std() method to calculate the
# standard deviation along the axis of the line
ageStandardDeviation = beautygroup['Idade'].std()

# Sort groups in ascending order of standard deviation
agestandardDeviationOrdered = ageStandardDeviation.sort_values()

# Print age homogeneity order by beauty class
# The closer to 0, the more homogeneous the group
print('Age homogeneity order by beauty class:')
print(agestandardDeviationOrdered)
