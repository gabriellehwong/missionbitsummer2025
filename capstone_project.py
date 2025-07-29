import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import time
import csv
import sys
import os


# sleep tracker lists
date_list = []
hours_list = []
energy_list = []


# Header row to format the .csv file nicely:
header = ['Date', 'Sleep Hours', 'Energy Levels']


def instructions():
    print("Loading...")
    time.sleep(3)
    print("\nWelcome to your Sleep and Habit Tracker!")
    print(
        "This is an online tracker that tracks the user's daily activities and habits such as fitness, mood, and sleep. Additionally, other organizational features include reminders, timers, and to-do lists."
    )
    input("\nPress enter to continue ")
    print("Loading...")
    time.sleep(3)


def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Sleep Tracker")
        print("2. Habit Tracker")
        print("3. To-Do List")
        print("4. Quit")
        user_choice = input("Enter a number: ")
        if user_choice == "1":
            print("Loading...")
            time.sleep(3)
            sleep_tracker()
        elif user_choice == "2":
            print("Loading...")
            time.sleep(3)
            habit_tracker()
        elif user_choice == "3":
            print("Loading...")
            time.sleep(3)
            todo_list()
        elif user_choice == "4":
            print("Exiting...")
            time.sleep(3)
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


def sleep_tracker():
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
        # wrapping our old while loop with another while True for the addiotona
        # menu aoptions
        print("\n--- Sleep Tracker ---")
        print("1. Log sleep data")
        print("2. View sleep chart")
        print("3. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            # getting our date inputs
            while True:
                month = input("\nWhat month is it? ").lower()

                if month not in days_and_months:
                    print("Invalid input.")
                    continue
                
                month_number_full = datetime.strptime(month, "%B").month
            
                try:
                    day = int(input("\nWhat day do you want to track (number)? "))
                    if not 1 <= day <= days_and_months.get(month):
                        # making use of our month-days dictionary
                        print(f"Invalid day. {month.title()} has {days_and_months[month]} days.")
                        continue
                    entry_date = datetime(datetime.now().year, month_number_full, day)
                    break
                except ValueError:
                    print("Invalid input.")

            while True:
                try:
                    hours_input = int(input("\nHow many hours of sleep did you get at night? "))

                    # similar to the energy level input conditional
                    if hours_input < 0 or hours_input > 24:
                        print("Please enter a realistic number of hours from 0-24.")
                        continue
                    break
                except ValueError:
                    print("Invalid input.")

            while True:        
                try:
                    energy_input = int(
                        input("\nOn a scale of 1-10, how much energy did you wake up with? ")
                    )
                    if not 1 <= energy_input <= 10:
                        print("Invalid input.")
                        continue
                    break
                except ValueError:
                    print("Invalid input.")

            save_sleep_data(entry_date, hours_input, energy_input)
            print(f"\nLogged: {hours_input} hours of sleep and {energy_input}/10 energy on {entry_date.strftime('%B %d, %Y')}")

        elif choice == "2":
            # loading and displaying the data into graphs!
            dates, hours, energy = load_sleep_data()

            # debugging before hand the issue we kept running into
            if not dates:
                print("No sleep data found. Log some data first please!")
                continue

            # creating the chart
            plt.figure(figsize=(10, 6))
            plt.subplot(2, 1, 1)
            plt.scatter(dates, hours, marker='o', color='blue', label='Sleep Hours')
            plt.title('Sleep Tracking Over Time')
            plt.ylabel('Hours of Sleep')
            plt.grid(True, alpha=0.3)
            plt.legend()
            
            plt.subplot(2, 1, 2)
            plt.scatter(dates, energy, marker='o', color='green', label='Energy Level')
            plt.ylabel('Energy Level (1-10)')
            plt.xlabel('Date')
            plt.grid(True, alpha=0.3)
            plt.legend()
            
            plt.tight_layout()
            plt.show()

        elif choice == "3":
            break
        else:
            print("Please enter a valid number.")


def view_habits():
    print("Current habits:", user_habits)
    input("Press enter to continue ")


def complete_habit():
    if not user_habits:
        print("No habits to track. Add some habits first!")
        return
    
    print("Available habits:")
    for i, habit in enumerate(user_habits, 1):
        print(f"{i}. {habit}")

    try:
        choice = int(input("Which habit did you complete today? Enter the number: ")) - 1
        if 0 <= choice <len(user_habits):
            print(f"Great! You completed: {user_habits[choice]}")
            user_habits.remove(user_habits[choice])
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")


# mood tracker habit lists
user_habits = []


def add_habit():
    habit_name = input("Enter the habit name you would like to add: ")
    user_habits.append(habit_name)
    print(f"Habit {habit_name} added successfully!")


def habit_tracker():
    while True:
        print("\n--- Habit Tracker ---")
        print("1. View Habits")
        print("2. Add Habit")
        print("3. Mark Habit as completed")
        print("4. Go back to Main Menu")

        try:
            habit_choice = int(input("Enter a number: "))
            if habit_choice == 1:
                view_habits()
            elif habit_choice == 2:
                add_habit()
            elif habit_choice == 3:
                complete_habit()
            elif habit_choice == 4:
                menu()
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def view_tasks():
    print("To-do List:", user_tasks)
    input("Press enter to continue ")


def complete_task():
    if not user_tasks:
        print("No tasks to track. Add some tasks first!")
        return
    
    print("Available tasks:")
    for i, task in enumerate(user_tasks, 1):
        print(f"{i}. {task}")

    try:
        choice = int(input("Which task did you complete today? Enter the number: ")) - 1
        if 0 <= choice <len(user_tasks):
            print(f"Great! You completed: {user_tasks[choice]}")
            user_tasks.remove(user_tasks[choice])
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")


# list of user's tasks
user_tasks = []


def add_task():
    task_name = input("Enter the task name you would like to add to your to-do list: ")
    user_tasks.append(task_name)
    print(f"Task {task_name} added successfully!")


def todo_list():
    while True:
        print("\n--- To-Do List ---")
        print("1. View To-Do List")
        print("2. Add To-Do")
        print("3. Mark item as compeleted")
        print("4. Go back to main menu")
        try:
            todo_choice = input("Enter a number: ")
            if todo_choice == "1":
                view_tasks()
            elif todo_choice == "2":
                add_task()
            elif todo_choice == "3":
                complete_task()
            elif todo_choice == "4":
                menu()
            else:
                    print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

# Every Python file has a built-in variable called __name__. 
# Python automatically sets this variable depending on how the file is being used:
# When you run a Python file directly (like python my_script.py), Python sets __name__ 
# to the string "__main__"
if __name__ == "__main__":
    instructions()
    menu()