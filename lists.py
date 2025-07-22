my_list = [
    [1, 2, 3],
    [4, 5, 6]
]
#print(my_list[len(my_list)])
print(my_list[-1][-1])
print(my_list[1][1])
'''
# creating empty list
favorite_youtubers = []
# adding to list
favorite_youtubers.append("OfflineTV")
favorite_youtubers.append("urmomsushi")
favorite_youtubers.append("Valkyrae")
favorite_youtubers.append("Odd1sOut")
favorite_youtubers.append("")
# using a for loop to print items
for youtuber in favorite_youtubers:
    print(youtuber)
# displaying an item
print(favorite_youtubers[0])
# modifying an item
favorite_youtubers[4] = "name"
# removing an item
favorite_youtubers.remove("name")
# sorting list
favorite_youtubers.sort()
#print length of list
print("Length of list:", len(favorite_youtubers))
# printing final list
print("Final list:", favorite_youtubers)
'''
even_list = [x for x in range(20) if x % 2 == 0]
print(even_list)

addition_list = [1,2,3,4,5]
addition_list = [num + 10 for num in addition_list]
print (addition_list)

ages_list = [17, 20, 46, 13, 29, 30, 15, 10]
new_ages_list = [age for age in ages_list if age >= 20]
print(new_ages_list)