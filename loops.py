stars = ["Vega", "Polaris", "Sirius", "Betelgeuse"]
for star in stars:
    print("Look up! You can see", star)

for i in range(5):
    print(str("*") * (i + 1))

for i in range(5):
    print(str(i + 1) * 5)

while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        print("Goodbye!")
        break  # exit the loop
    else:
        print("You typed:", text)