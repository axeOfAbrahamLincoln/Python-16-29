import pandas

data = pandas.read_csv("day 25/weather project/weather_data.csv")

# temperature_data = data["temp"]

# list_temperature = temperature_data.to_list()

# avg_temp = sum(list_temperature) / len(list_temperature)
# print(avg_temp)

# avg_temp = data["temp"].mean()
# print(avg_temp)

# max_temp = data.temp.max()

# row = data[data.temp == max_temp]
# print(row)


monday = data[data.day == "Monday"]
print(monday)


monday_temp = monday.temp[0]
print(monday_temp)