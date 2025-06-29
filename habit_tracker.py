import json
import os
from datetime import datetime, timedelta

def current_time():
    """Return the current date and time as a datetime object."""
    return datetime.now()

def load_habits():
    """
    Load habits from 'habits.json' if it exists.
    Converts 'last_done' strings back to datetime objects.
    Returns a list of habit dictionaries.
    """
    if os.path.exists("habits.json"):
        with open("habits.json", "r") as f:
            try:
                data = json.load(f)
                for habit in data:
                    habit["last_done"] = datetime.fromisoformat(habit["last_done"])
                return data
            except json.JSONDecodeError:
                return []
    return []

def add_habit(user_habit):
    """
    Add a new habit to the list with a streak of 0 and current timestamp.
    Automatically saves the updated list to file.
    """
    for habit in habits:
        if habit["habit_name"] == user_habit:
            print("Habit already exists!")
            return
    current_habit = {"habit_name": user_habit, "streak": 0, "last_done": current_time()} 
    habits.append(current_habit)
    save_habits()
    print("Successfully added new habit!")

def mark_habit_done(index):
    """
    Mark a habit as done by its 1-based index (input by user).
    Updates streak based on time difference and saves the updated data.
    """
    if 0 < index <= len(habits):
        index -= 1
        print(check_streak(index))
        save_habits()
    else:
        print("Habit not found!")

def view_habits():
    """Display all stored habits with their streak count and last completion time."""
    if (len(habits) == 0):
        print("\nNo habits found!")
    else:
        print("\n--------------All Habits--------------")
        for i, habit in enumerate(habits):
            print(f"{i + 1}. {habit.get('habit_name')} - Streak: {habit.get('streak')} - Last Done: {habit.get('last_done').strftime('%a %d %b %Y, %I:%M%p')}")
        print("--------------------------------------")

def check_streak(index):
    """
    Compare the current date with the last completion date of the habit.
    Updates the streak:
        - Resets if > 1 day missed
        - Increments if exactly 1 day passed
        - Warns if already marked today
    Returns a status message.
    """
    last = habits[index]["last_done"] 
    now = current_time()
    difference = (now.date() - last.date()).days
    if difference > 1: # Not being strict with the time i.e. precisely 24h for the streak to retain
        habits[index]["streak"] = 1
    elif difference == 1:
        habits[index]["streak"] += 1
    elif difference == 0: return "You've already logged this habit today!"
    habits[index]["last_done"] = current_time()
    return (f"Habit marked done successfully! Your current streak is {habits[index]['streak']}.")

def edit_habit(index, new_name):
    if 0 < index <= len(habits):
        habits[index - 1]['habit_name'] = new_name
        print("Habit modified successfully!")
        save_habits()
    else:
        print("Habit not found!")

def delete_habit(index):
    if 0 < index <= len(habits):
        habits.pop(index - 1)
        print("Habit deleted successfully!")
        save_habits()
    else:
        print("Habit not found!")

def save_habits():
    """
    Save the current list of habits to 'habits.json'.
    Converts datetime objects to ISO-formatted strings for JSON compatibility.
    """
    formatted_habits = []
    for habit in habits:
        formatted_habit = {
            "habit_name": habit["habit_name"],
            "streak": habit["streak"],
            "last_done": habit["last_done"].isoformat()
        }
        formatted_habits.append(formatted_habit)

    with open("habits.json", "w") as f:
        json.dump(formatted_habits, f, indent = 4)


habits = load_habits()
while True:
    user_input = input("""
1. Add Habit
2. Mark Habit as Done
3. View Habits and Streaks
4. Edit Habit
5. Delete Habit
6. Exit\n
""")

    match (user_input):
        case "1":
            input_habit = input("\nWhat habit would you like to store? ").strip()
            if not input_habit:
                print("Habit name cannot be empty!")
                continue
            add_habit(input_habit)

        case "2":
            if (len(habits) == 0):
                print("\nNo habits found!")
            else:
                try:
                    habit_index = int(input("\nWhich habit would you list to mark as done? (Input the serial number) "))
                    mark_habit_done(habit_index)
                except (ValueError):
                    print("Invalid input!")

        case "3":
            view_habits()

        case "4":
            if (len(habits) == 0):
                print("\nNo habits found!")
            else:
                try:
                    habit_index = int(input("\nWhich habit would you like to edit? (Input the serial number) "))
                    while True:
                        new_habit_name = input("\nWhat would you like to rename it to? ").strip()
                        if not new_habit_name:
                            print("Habit name cannot be empty!")
                            continue
                        edit_habit(habit_index, new_habit_name)
                        break
                except (ValueError):
                    print("Invalid input!")

        case "5":
            if (len(habits) == 0):
                print("\nNo habits found!")
            else:
                try:
                    habit_index = int(input("\nWhich habit would you like to delete? (Input the serial number) "))
                    delete_habit(habit_index)
                except (ValueError):
                    print("Invalid input!")

        case "6":
            print("\nSaved and Exited successfully.")
            save_habits()
            exit()

        case _:
            print("\nInvalid input! Try again.")