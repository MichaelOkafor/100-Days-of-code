# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# this changes the data to dictionary
data_dict = data.to_dict()
print(data_dict)

# this changes a column in the data to list
data_list = data["temp"].to_list()
print(data_list)

print(data["temp"].mean())  # to get the average temperature
print(data["temp"].max())  # to get the maximum temperature

# to get data from columns
print(data["condition"])
# OR
print(data.condition)

# to get data from row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])  # this is to check the column with the highest temp

monday = data[data.day == "Monday"]
print(monday.condition)

# converting mondays temp to Celsius
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
temp_celsius = (monday_temp * 9/5) + 32
print(temp_celsius)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Sheldon", "Lenard", "Rajesh"],
    "scores": [82, 88, 81, 83],
}
data = pandas.DataFrame(data_dict)  # this creates a new csv file
data.to_csv("new_data.csv")
