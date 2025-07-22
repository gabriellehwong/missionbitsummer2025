'''
try:
    # Code that might cause an error
    value = int(input("Enter a number: "))
    print("You entered:", value)
except ValueError:
    # Code that runs if an error happens
    print("Oops! That was not a valid number.")
'''
valid_numbers = []
inputs = ["10", "20", "", "abc", "30", "40", "xyz"]

for num in inputs:
    try:
        num = float(num)
        valid_numbers.append(num)
    except ValueError:
        continue

print(valid_numbers)