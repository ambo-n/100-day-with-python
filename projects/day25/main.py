import pandas
# data=pandas.read_csv("weather_data.csv")

# monday = data[data.day =="Monday"]
# monday_temp_in_f =monday.temp[0]*9/5 +32
# print(monday_temp_in_f)

squirrel_data = pandas.read_csv("squirrel_data.csv")
# fur_data = squirrel_data["Primary Fur Color"].to_list()
# fur_colour =[]
# count =[]

# number_of_gray =0
# number_of_cinnamon =0
# number_of_black =0
# for element in fur_data:
#     if pandas.isna(element):
#         continue
#     if element not in fur_colour:
#         fur_colour.append(element)
#     if element == 'Gray':
#         number_of_gray +=1
#     elif element == 'Cinnamon':
#         number_of_cinnamon+=1
#     elif element == 'Black':
#         number_of_black +=1
# count.extend([number_of_gray, number_of_cinnamon,number_of_black])

# fur_data_dict ={'Fur Colour':fur_colour, 'Count':count}

# squirrel_count = pandas.DataFrame(fur_data_dict)

# squirrel_count.to_csv("squirrel_count.csv")

fur_counts = squirrel_data['Primary Fur Color'].value_counts()
squirrel_count = fur_counts.reset_index()
squirrel_count.columns=['Fur Colour','Count']
squirrel_count.to_csv("squirrel_count.csv")
