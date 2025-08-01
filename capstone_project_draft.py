import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import time
import csv
import sys
import os

# sleep tracker lists
days_list = []
hours_list = []
energy_list = []

# Header row to format the .csv file nicely:
header = ['Date', 'Sleep Hours', 'Energy Levels']

def instructions():
    print("Loading...")
    time.sleep(3)
    print("Welcome to [title]!")
    print("[title] is an online tracker that tracks the user’s daily activities and habits. Additionally, other organizational features include to-do lists.")
    input("Press enter to continue ")


def menu():
    while True:
        print("\nMenu:")
        print("1. Sleep Tracker")
        print("2. Habit Tracker")
        print("3. To-Do List")
        print("4. Quit")
        user_choice = input("Enter a number: ")
        if user_choice == "1":
            sleep_tracker()
        elif user_choice == "2":
            habit_tracker()
        elif user_choice == "3":
            todo_list()
        elif user_choice == "4":
            print("Exiting...")
            sys.exit()
        else:
            print("Please enter a valid number.")

def save_sleep_data(date, hours, energy, filename="sleep_data.csv"):
    """Save a single sleep entry to CSV file. Will usually be named sleep_data.csv
    For the MVP, we are just working on getting a coherent user experience. Then later
    we will work on saving individuals profiles/data. 
    """
    # Check if file exists, if not create it with headers! 
    file_exists = os.path.exists(filename)
    
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([date.strftime('%Y-%m-%d'), hours, energy])

def load_sleep_data(filename="sleep_data.csv"):
    """Load existing sleep data from CSV file. This code will
    come in handy for when we want to plot! This is a. neater way
    of extracting the data we collected to then send it for visual
    analysis. 
    """
    if not os.path.exists(filename):
        # if the filename does not exist, then instead of 
        # crashing the script we work around this by simply
        # returning empty lists
        return [], [], []
    
    dates, hours, energy = [], [], []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(datetime.strptime(row['Date'], '%Y-%m-%d'))
            hours.append(int(row['Sleep Hours']))
            energy.append(int(row['Energy Levels']))
    return dates, hours, energy


    
def save_analysis(results, filename):
    with open(filename, "w") as file:
        for data in results:
            file.write(str(f"{data.title()}: {results.get(data)}"))


def sleep_tracker():
    print("\n--- Sleep Tracker ---")
    days_and_months = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31,
    }
    while True:
        month = input("What month is it? ").lower()
        if month not in days_and_months:
            print("Invalid input.")
            continue
        try:
            day = int(input("What day do you want to track (number)? "))
            if not 1 <= day <= days_and_months.get(month):
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")
            continue
        days_list.append(day)
        try:
            hours_input = int(input("How many hours of sleep did you get at night? "))
        except ValueError:
            print("Invalid input.")
            continue
        try:
            energy_input = int(
                input("On a scale of 1-10, how much energy did you wake up with? ")
            )
            if not 1 <= energy_input <= 10:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")
        break

    today = str(datetime.now().date())
    hours_list.append(hours_input)
    energy_list.append(energy_input)
    entry = {"date": today, "hours": hours_list, "energy": energy_list}
    print(f"Logged: {hours_input} hours on {today}.")
    print(entry)
    save_analysis(entry, "test.csv")
    x = np.array(days_list)
    y = np.array(hours_list)
    plt.title("Sleep Tracker")
    # plt.xlabel(f"Days of {month.title()}")
    plt.ylabel("Hours")
    plt.scatter(x, y)
    plt.show()
    # while True:
    #     input = input("Press 1 to go back to the menu or 2 to track another date ")
    #     if input == "1":
    #         menu()
    #     elif input == "2":
    #         sleep_tracker()
    #     else:
    #         print("Invalid input.")


def view_tracker():
    print(user_habits)
    input("Press Enter to Continue.")
    habit_tracker()


def track_habit():
    pass


# mood tracker habit lists
user_habits = []


def add_habit():
    habit_name = input("Enter the habit name you would like to add: ")
    user_habits.append(habit_name)
    print(f"Habit {habit_name} added successfully")
    input("Press Enter to Continue")
    habit_tracker()


def habit_tracker():
    print("\n--- Habit Tracker Menu ---")
    print("\n1. View Habits")
    print("2. Mark Habit as completed")
    print("3. Add Habit")
    print("4. Go back to Main Menu")
    while True:
        habit_choice = int(input("Enter a number: "))
        if habit_choice == 1:
            view_tracker()
        elif habit_choice == 2:
            track_habit()
        elif habit_choice == 3:
            add_habit()
        elif habit_choice == 4:
            menu()
        else:
            print("Please enter a valid number.")


def todo_list():
    print("--- To-Do List ---")
    print("\n1. Add To-Do")
    print("2. View To-Do List")
    print("3. Mark item as compeleted")
    print("4. Go back to main menu")
    while True:
        todo_choice = input("Please enter a number.")
        if todo_choice == "1":
            pass
        elif todo_choice == "2":
            pass
        elif todo_choice == "3":
            pass
        elif todo_choice == "4":
            menu()
        else:
            print("Please print a valid number")


instructions()
menu()
