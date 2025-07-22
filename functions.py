'''
def greet_customer():
    print("Welcome to Manny’s grocery store.")
    print("Our special is red bell peppers.")
    print("Ask if you need anything")
greet_customer()

def greet_customer():
   print("Welcome to Manny’s grocery store.")
   print("Our special is red bell peppers.")
   print("Ask if you need anything!")
print("Cleanup on aisle 6")
greet_customer()
greet_customer()
'''
def greet_customer(special_today: str, grocery_store: str):
   print("Welcome to " + grocery_store + ".")
   print("Our special is " + special_today + ".")
   print("Ask if you need anything!")
greet_customer("pickles", "Manny’s grocery store")

def function(parameter1, parameter2):
   print(parameter1)
   print(parameter2)
function("hello", "world")

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
print(type(square_point(1, 3)))