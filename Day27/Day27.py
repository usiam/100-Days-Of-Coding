import csv

with open('weather_data.csv') as csvFile:
    weatherData = csvFile.readlines()
    weatherData = [line.strip('\n') for line in weatherData]
    print(weatherData)

with open('weather_data.csv') as csvFile:
    data = csv.reader(csvFile)
    temperatures = [int(row[1]) for row in data if row[1] != 'temp']
    print(temperatures)

import pandas as pd

data = pd.read_csv('weather_data.csv')
data_dict = data.to_dict()
temp = data['temp']
tempList = temp.to_list()
#
print(data_dict)
print(tempList)
print(round(temp.mean(), 2))
print(temp.max())

# reading a column
col = data['condition']
# or
print(data.condition)

# reading a row
print(data[data.day == 'Monday']) # print the data when the data tables attribute is Monday

# get the row with the highest temp
print(data[data.temp == temp.max()]) # prints the row in the DataFrame data where the DataFrame's temp attribute is
#                                     # equal to the maximum in the temp column/series

monday = data[data.day == 'Monday']
print(monday.condition)

mondayFTemp = int(monday.temp) * (9 / 5) + 32
print(mondayFTemp)

# dict to DataFrame

dataDict = {
    'students': ['Amy', 'Joe', 'Alex'],
    'scores': [94, 20, 84]
}
dataFrame = pd.DataFrame(dataDict)
dataFrame.to_csv('studentScore.csv')