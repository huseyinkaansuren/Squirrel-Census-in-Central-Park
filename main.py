import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sum_of_gray = sum(data["Primary Fur Color"] == "Gray")
sum_of_black = sum(data["Primary Fur Color"] == "Black")
sum_of_cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")

data_dict = {
    "Fur Color":["Gray", "Black", "Cinnamon"],
    "Count":[sum_of_gray,sum_of_black,sum_of_cinnamon]
}
data_file = pandas.DataFrame(data_dict)
data_file.to_csv("squirrel_count.csv")
print(data_file)