user_input = "Python"
if user_input == "python":
    print("Match!")
else:
    print("No match.")

user_input = "Python"
if user_input.lower() == "python":
    print("Match!")
else:
    print("No match.")

fruits = ["apple", "banana", "cherry", "date"]

user_input = input("Enter a fruit name: ")

# TODO: Convert user_input to lowercase
lowercase_input = user_input.lower()
# TODO: Check if lowercase user_input is in fruits list
if lowercase_input in fruits:
# TODO: Print the appropriate message
    print("Fruit found!")
else:
    print("Fruit not found!")

data = "apple,banana,cherry"
# Split data by comma and save the result
words = data.split(",")
# Print the result
print(words)

data = "Apple, Banana, Cherry"
fruits = data.split(",")
print(fruits) # split() without strip()

clean_fruits = [] 

for fruit in fruits:
    clean_fruits.append(fruit.strip())  

print(clean_fruits) # split() with strip()