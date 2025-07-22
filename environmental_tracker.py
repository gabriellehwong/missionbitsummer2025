prompts = ["the number of showers you take per week", "how long your average showers are (in minutes)", "the number of meals you eat per week"]

print("\nEnvironmental Tracker")

# shower tracker
print("\nShower Tracker")
num_showers = int(input("Enter the number of showers you take per week: "))
len_showers = int(input("Enter how long your average showers are (in minutes): "))
water_per_5_min = 10
water_per_min = water_per_5_min / 5
water_per_shower = len_showers * water_per_min
water_per_week = num_showers * water_per_shower
print("You take", num_showers, "showers per weeek, and your average showers are", len_showers, "minutes long.")
print("Your total water consumption per shower is", water_per_shower, "gallons of water.")
print("Your total water consumption per week is", water_per_week, "gallons of water.")

# meal tracker
print("\nMeal Tracker")
num_meals = int(input("Enter the number of meals you eat per week: "))
co2_per_meal = 3
co2_per_week = num_meals * co2_per_meal
print("Your total carbon footprint per week is", co2_per_week, "kilograms of CO2.")

# mile tracker
print("\nMile Tracker")
num_miles = int(input("Enter the number of miles you travel per week: "))
co2_per_mile = 0.4
co2_per_week += num_miles * co2_per_mile
print("Your total carbon footprint per week is now", co2_per_week, "kilograms of CO2.")

# summary
print("\nSummary")
print("Total water consumption per week:", water_per_week)
print("Total carbon footprint per week:", co2_per_week)