import pandas

data = pandas.read_csv("day 25/squirrel project/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_fur_color_data = data["Primary Fur Color"].value_counts()

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(gray_squirrels)

squirrel_fur_color_data.to_csv("day 25/squirrel project/color_count.csv")


