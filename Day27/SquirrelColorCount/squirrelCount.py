import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# Gray, Cinnamon, Black

furColors = ['Gray', 'Cinnamon', 'Black']
colorCount = [len(data[data['Primary Fur Color'] == 'Gray']), len(data[data['Primary Fur Color'] == 'Cinnamon']), len(data[data['Primary Fur Color'] == 'Black']) ]

furColorCount = {
    'Fur Color' : furColors,
    'Count' : colorCount
}

newData = pandas.DataFrame(furColorCount)
newData.to_csv('color_count.csv')