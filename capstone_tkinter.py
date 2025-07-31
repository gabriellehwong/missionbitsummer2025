import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import os
import pandas as pd

# our global data storage
# i think in another scenario or if there was more time, we could do this better
# because we also need to consider different users. 
user_habits = []
user_tasks = []

class HabitTrackerApp(tk.Tk):
    """Main app controller, will help with managing which page is currently shown."""
    # *args collects any positional arguments into a tuple
    # **kwargs collects any keyword args into a dictionary
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # configuring the main window
        self.title("Sleep and Habit Tracker")
        self.geometry("800x600")
        self.configure(bg="#221B26")

        # creating container to hold all the pages
        container = tk.Frame(self, bg="#221B26")
        container.pack(side="top", fill="both", expand=True)

        # configure grid weights so pages can expand properly
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary to store page instances
        self.frames = {}

        # creating al the pages and storing them in the frames dictionary.
        # we define which pages the app will have here!
        for PageClass in (MainMenuPage, SleepTrackerPage, HabitTrackerPage, TodoListPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame

            # all the frames occupy the same grid positon (stacked on top of each other)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenuPage")

    def show_frame(self, page_name):
        """Bring the specified page to the front"""
        frame = self.frames[page_name] # accessing a dictionary
        frame.tkraise() # .tkraise() brings the frame to the top of the stack!

class MainMenuPage(tk.Frame):
    """This is the equivalent to the menu() function in the CLI version""" 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#c29bd2")
        self.controller = controller

        # Title
        title_label = tk.Label(self, text="Sleep and Habit Tracker",
                               font=("Arial", 24, "bold"),
                               # as you can see from this green color, the textbox comes out as green in contrast with the overall purple
                               bg="#c29bd2", fg="#ecf0f1")    
        
        title_label.pack(pady=50)

        # subtitles
        subtitle_label = tk.Label(self, text="Track your sleep, habits, and to-dos to improve your life ⋅˚₊‧ ୨୧ ‧₊˚ ⋅")
        subtitle_label.pack(pady=10)

        # button frame for nice spacing
        button_frame = tk.Frame(self, bg="#c29bd2")
        button_frame.pack(pady=50)

        # navigation buttons - each one switches to a diff page
        sleep_btn = tk.Button(button_frame, text="ᶻ z 𐰁₊˚⋆ Sleep Tracker",
                              command=lambda: controller.show_frame("SleepTrackerPage"),
                              font=("Arial", 14, "bold"), fg="#668c5f",
                              width=20, height=2)
        sleep_btn.pack(pady=10)

        habit_btn = tk.Button(button_frame, text="⭒˚｡⋆‧₊˚✩彡 Habit Tracker",
                              command=lambda: controller.show_frame("HabitTrackerPage"),
                              font=("Arial", 14, "bold"), fg="#668c5f",
                              width=20, height=2)
        habit_btn.pack(pady=10)

        todo_btn = tk.Button(button_frame, text="‧₊˚🖇️✩ ₊˚🎧⊹♡ To-Do List",
                              command=lambda: controller.show_frame("TodoListPage"),
                              font=("Arial", 14, "bold"), fg="#658e5d",
                              width=20, height=2)
        todo_btn.pack(pady=10)

        quit_btn = tk.Button(button_frame, text="Quit", 
                            command=self.controller.quit,
                            font=("Arial", 14, "bold"), bg="#95a5a6", fg="red",
                            width=20, height=2)
        quit_btn.pack(pady=10)

class SleepTrackerPage(tk.Frame):
    """Sleep trackin page, we are converting sleep_tracker function to GUI!"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#2c3e50')
        self.root = parent
        self.controller = controller
        
        # Page title
        title_label = tk.Label(self, text="ᶻ z 𐰁₊˚⋆ Sleep Tracker", 
                              font=("Arial", 20, "bold"), 
                              bg='#2c3e50', fg='#ecf0f1')
        title_label.pack(pady=20)
        
        # Input section
        input_frame = tk.Frame(self, bg='#34495e', relief='raised', bd=2)
        input_frame.pack(pady=20, padx=50, fill='x')
        
        # Month selection
        tk.Label(input_frame, text="Month:", font=("Arial", 12), 
                bg='#34495e', fg='#ecf0f1').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        
        self.month_var = tk.StringVar()
        month_combo = ttk.Combobox(input_frame, textvariable=self.month_var, width=15)
        month_combo['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                                'July', 'August', 'September', 'October', 'November', 'December')
        month_combo.grid(row=0, column=1, padx=10, pady=10)
        month_combo.set('July')
        
        # Day selection
        tk.Label(input_frame, text="Day:", font=("Arial", 12), 
                bg='#34495e', fg='#ecf0f1').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        
        self.day_var = tk.StringVar()
        day_spinbox = tk.Spinbox(input_frame, from_=1, to=31, textvariable=self.day_var, width=18)
        day_spinbox.grid(row=1, column=1, padx=10, pady=10)
        
        # Sleep hours
        tk.Label(input_frame, text="Hours of Sleep:", font=("Arial", 12), 
                bg='#34495e', fg='#ecf0f1').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        
        self.hours_var = tk.StringVar()
        hours_spinbox = tk.Spinbox(input_frame, from_=0, to=24, textvariable=self.hours_var, width=18)
        hours_spinbox.grid(row=2, column=1, padx=10, pady=10)
        
        # Energy level
        tk.Label(input_frame, text="Energy Level (1-10):", font=("Arial", 12), 
                bg='#34495e', fg='#ecf0f1').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        
        self.energy_var = tk.StringVar()
        energy_spinbox = tk.Spinbox(input_frame, from_=1, to=10, textvariable=self.energy_var, width=18)
        energy_spinbox.grid(row=3, column=1, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        log_btn = tk.Button(button_frame, text="📝 Log Sleep Data", 
                           command=self.log_sleep_data,
                           font=("Arial", 12, "bold"), bg='#3498db', fg='black')
        log_btn.pack(side='left', padx=10)
        
        chart_btn = tk.Button(button_frame, text="📊 View Chart", 
                             command=self.show_chart,
                             font=("Arial", 12, "bold"), bg='#9b59b6', fg='black')
        chart_btn.pack(side='left', padx=10)
        
        back_btn = tk.Button(button_frame, text="Back to Menu", 
                            command=lambda: controller.show_frame("MainMenuPage"),
                            font=("Arial", 12, "bold"), bg='#95a5a6', fg='black')
        back_btn.pack(side='left', padx=10)
        
        # Status label
        self.status_label = tk.Label(self, text="Ready to log sleep data", 
                                    font=("Arial", 10), bg='#2c3e50', fg='#bdc3c7')
        self.status_label.pack(pady=10)
        
    def log_sleep_data(self):
        """Save sleep data to CSV file, but for gui"""
        try:
            # Validate inputs
            month_name = self.month_var.get() # input() == .get() 
            day = int(self.day_var.get())
            hours = int(self.hours_var.get())
            energy = int(self.energy_var.get())
            
            if not month_name:
                raise ValueError("Please select a month")
            
            if not (1 <= day <= 31):
                raise ValueError("Day must be between 1 and 31")
                
            if not (0 <= hours <= 24):
                raise ValueError("Hours must be between 0 and 24")
                
            if not (1 <= energy <= 10):
                raise ValueError("Energy level must be between 1 and 10")
            
            # Create date object
            month_number = datetime.strptime(month_name, "%B").month
            entry_date = datetime(datetime.now().year, month_number, day)
            
            # Save to CSV
            self.save_sleep_data(entry_date, hours, energy)
            
            # Update status
            self.status_label.config(text=f"Logged: {hours} hours, {energy}/10 energy on {month_name} {day}")
            
            # Clear inputs for next entry
            self.hours_var.set("")
            self.energy_var.set("")
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def save_sleep_data(self, date, hours, energy, filename="sleep_data.csv"):
        """Save sleep entry to CSV file"""
        file_exists = os.path.exists(filename)
        header = ['Date', 'Sleep Hours', 'Energy Levels']
        
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)
            writer.writerow([date.strftime('%Y-%m-%d'), hours, energy])
    
    def load_sleep_data(self, filename="sleep_data.csv"):
        """Load and sort sleep data using pandas might be the fix
        for the viz issues."""
        if not os.path.exists(filename):
            return [], [], []
        
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')  # Sort by date using pandas .sort_values()
        
        return df['Date'].tolist(), df['Sleep Hours'].tolist(), df['Energy Levels'].tolist()
    
    def show_chart(self):
        """Display sleep data in a new window with matplotlib chart"""
        dates, hours, energy = self.load_sleep_data()
        
        if not dates:
            messagebox.showinfo("No Data", "No sleep data found. Log some data first!")
            return
        
        # Create new window for chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Sleep Chart")
        chart_window.geometry("800x600")
        chart_window.configure(bg='#2c3e50')
        
        # Create matplotlib figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), facecolor='white')
        
        # Sleep hours plot
        # Was able to change the visuals to bar plotting!
        ax1.bar(dates, hours, color='#3498db')
        ax1.set_title('Sleep Hours Over Time', color='black', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Hours of Sleep', color='white')
        ax1.grid(True, alpha=0.3)
        ax1.set_facecolor('white')
        ax1.tick_params(colors='black')
        
        # Energy levels plot
        ax2.bar(dates, energy, color='#2ecc71')
        ax2.set_title('Energy Levels Over Time', color='black', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Energy Level (1-10)', color='black')
        ax2.set_xlabel('Date', color='black')
        ax2.grid(True, alpha=0.3)
        ax2.set_facecolor('white')
        ax2.tick_params(colors='black')
        
        plt.tight_layout()
        
        # Embed plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Add close button
        close_button = ttk.Button(chart_window, text="Close Chart", 
                                 command=chart_window.destroy, style='Custom.TButton')
        close_button.pack(pady=10)

class HabitTrackerPage(tk.Frame):
    """Habit tracking page where we gui-fy habit_tracker()"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#5227b8")
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="⭒˚｡⋆‧₊˚✩彡 Habit Tracker", 
                              font=("Arial", 20, "bold"), 
                            fg="#8661dd")
        title_label.pack(pady=20)
        
        # Add habit section
        add_frame = tk.Frame(self, bg="#8661dd", relief='raised', bd=2)
        add_frame.pack(pady=10, padx=50, fill='x')
        
        tk.Label(add_frame, text="Add New Habit:", font=("Arial", 12, "bold"), 
                bg="#8661dd", fg='#ecf0f1').pack(pady=10)
        
        self.habit_entry = tk.Entry(add_frame, font=("Arial", 12), width=30)
        self.habit_entry.pack(pady=5)
        
        add_btn = tk.Button(add_frame, text="Add Habit", 
                           command=self.add_habit,
                           font=("Arial", 10, "bold"))
        add_btn.pack(pady=10)
        
        # Habits display section
        display_frame = tk.Frame(self, bg="#8661dd", relief='raised', bd=2)
        display_frame.pack(pady=10, padx=50, fill='both', expand=True)
        
        tk.Label(display_frame, text="Your Habits:", font=("Arial", 12, "bold"), 
                 bg="#8661dd", fg='#ecf0f1').pack(pady=10)
        
        # Scrollable listbox for habits
        self.habits_listbox = tk.Listbox(display_frame, font=("Arial", 11), height=8)
        self.habits_listbox.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Complete habit button
        complete_btn = tk.Button(display_frame, text="Mark as Completed ᯓ★", 
                                command=self.complete_habit,
                                font=("Arial", 10, "bold"), bg="#61a867")
        complete_btn.pack(pady=10)
        
        # Navigation
        nav_frame = tk.Frame(self, bg='#2c3e50')
        nav_frame.pack(pady=20)
        
        back_btn = tk.Button(nav_frame, text="Back to Menu", 
                            command=lambda: controller.show_frame("MainMenuPage"),
                            font=("Arial", 12, "bold"), bg="#61a867")
        back_btn.pack()
        
        # Refresh the habits list when page loads
        self.refresh_habits_list()

    # def add_habit():
    # habit_name = input("Enter the habit name you would like to add: ")
    # user_habits.append(habit_name)
    # print(f"Habit {habit_name} added successfully")
    def add_habit(self):
        """Add a new habit to the list"""
        # habit_entry is a tkinter widget, a text input box where users can type
        habit_name = self.habit_entry.get().strip() # removes any leading, and trailing whitespaces we could also use .lower if you want
        # here i am checking for the edge case where they hit enter without actually inputting anything (basically blank space)
        if habit_name:
            user_habits.append(habit_name)
            self.habit_entry.delete(0, tk.END) # making the input box blank again for the next item
            self.refresh_habits_list()
            messagebox.showinfo("Success", f"Add habit: {habit_name}")
        else:
            messagebox.showwarning("Warning", "Please enter a habit name")

    def complete_habit(self):
        """Mark selected habit as completed"""
        selection = self.habits_listbox.curselection()
        if selection:
            index = selection[0]
            completed_habit = user_habits[index]
            # remove the habit (same as og code)
            user_habits.remove(completed_habit)
            self.refresh_habits_list()
            messagebox.showinfo("Great job!", f"Completed: {completed_habit}")
        else:
            messagebox.showwarning("Warning", "Please select a habit to complete")

    def refresh_habits_list(self):
        """Update the habits display"""
        self.habits_listbox.delete(0, tk.END)
        for habit in user_habits:
            self.habits_listbox.insert(tk.END, habit)

class TodoListPage(tk.Frame):
    """To-do list page - converts todo_list() function to GUI"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#a9d385") # this will change the back ground of the whole page
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="📝 To-Do List", 
                              font=("Arial", 20, "bold"), 
                              #if bg is not changes to the one in configure you will see a box with this color around the title
                              bg="#91aa7b", fg='#ecf0f1') 
        title_label.pack(pady=20)
        
        # Add task section
        add_frame = tk.Frame(self, bg="#bff28c", relief='raised', bd=2) # bg here changes the color in the first box at the top of this page
        add_frame.pack(pady=10, padx=50, fill='x')
        
        tk.Label(add_frame, text="Add New Task:", font=("Arial", 12, "bold"), 
                 # fg here will change color of the text
                bg="#bff28c", fg="#5858cc").pack(pady=10) # bg will make sure the textbox of "add new task" is the same as above or diff
        
        self.task_entry = tk.Entry(add_frame, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=5)
        
        add_btn = tk.Button(add_frame, text="Add Task", 
                           command=self.add_task,
                           font=("Arial", 10, "bold"), bg="#bff28c")
        add_btn.pack(pady=10)
        
        # Tasks display section
        display_frame = tk.Frame(self, bg="#bff28c", relief='raised', bd=2)
        display_frame.pack(pady=10, padx=50, fill='both', expand=True)
        
        tk.Label(display_frame, text="Your Tasks:", font=("Arial", 12, "bold"), 
                bg="#bff28c", fg="#5858cc").pack(pady=10)
        
        # Scrollable listbox for tasks
        self.tasks_listbox = tk.Listbox(display_frame, font=("Arial", 11), height=8)
        self.tasks_listbox.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Complete task button
        complete_btn = tk.Button(display_frame, text="Mark as Completed", 
                                command=self.complete_task,
                                font=("Arial", 10, "bold"), bg='#f39c12')
        complete_btn.pack(pady=10)
        
        # Navigation
        nav_frame = tk.Frame(self, bg='#2c3e50')
        nav_frame.pack(pady=20)
        
        back_btn = tk.Button(nav_frame, text="Back to Menu", 
                            command=lambda: controller.show_frame("MainMenuPage"),
                            font=("Arial", 12, "bold"), bg='#95a5a6')
        back_btn.pack()
        
        # Refresh the tasks list when page loads
        self.refresh_tasks_list()

# def add_task():
#     task_name = input("Enter the task name you would like to add to your to-do list: ")
#     user_tasks.append(task_name)
#     print(f"Task {task_name} added successfully!")
    def add_task(self):
        """Very similar to our other list-like features"""
        task_name = self.task_entry.get().strip()
        if task_name:
            user_tasks.append(task_name)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks_list()
            messagebox.showinfo("Success", f"Added task: {task_name}")
        else:
            messagebox.showwarning("Warning", "Please enter a task name")

    def complete_task(self):
        """Marking a task we select as completed"""
        selection = self.tasks_listbox.curselection()
        if selection:
            index = selection[0]
            completed_task = user_tasks[index]
            # Remove the task (same behavior as original code)
            user_tasks.remove(completed_task)
            self.refresh_tasks_list()
            messagebox.showinfo("Great Job!", f"Completed: {completed_task}")
        else:
            messagebox.showwarning("Warning", "Please select a task to complete")

    def refresh_tasks_list(self):
        """Update the tasks display"""
        self.tasks_listbox.delete(0, tk.END)
        for task in user_tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = HabitTrackerApp()
    app.mainloop()