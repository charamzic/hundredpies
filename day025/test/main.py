# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)  # Skip the first row
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)

list = data["temp"].to_list()
# print(list)
average = sum(list) / len(list)
# print(average)

# data["temp"].mean()

# max = data["temp"].max()
# print(max)

# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9 / 5 + 32
# print(f"Monday's temperature in Farenheit is: { monday_temp_f }")

data_dict = {"students": ["Amy", "James", "Pepa"], "scores": [76, 54, 81]}
converted_dict = pandas.DataFrame(data_dict)
# print(converted_dict)

# creates csv file
converted_dict.to_csv("new_data.csv")
