"""
# Creating a dictionary
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}

# Printing the dictionary
print(country_capitals)
print(country_capitals["United States"])
print(country_capitals["Italy"])
print(country_capitals["England"])
print(country_capitals.get("United States"))
print(country_capitals.get("Italy"))
print(country_capitals.get("England"))
"""

country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Naples",
    "England": "London",
}

# Change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"

print(country_capitals)

# Delete item having "United States" key
del country_capitals["United States"]

print(country_capitals)
"""
country_capitals.pop("Italy")
print(country_capitals)

country_capitals.update()
print(country_capitals)

country_capitals.clear()
print(country_capitals)

country_capitals.keys()
print(country_capitals)

country_capitals.values()
print(country_capitals)

country_capitals.get()
print(country_capitals)

country_capitals.popitem()
print(country_capitals)

country_capitals.copy()
print(country_capitals)

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

for k,v in country_capitals.items():
   print(k,v)


student = {"name": "Izzy", "age": "100"}
print(student.keys())
student["age"] = "19"
print(student)
student["grade"] = "A"
print(student)
print(student["school"])
"""
fruits = ["apple", "banana", "cherry", "date"]
person = {
    "name": "Bob", 
    "age": 25, 
    "city": "Chicago"
}

print(fruits[2])
print(person["age"])

dict = {"name": "Alice"}
# print(dict["age"])
print(dict.get("age"))

word = "hello"
print(word.upper())
print(type(word))