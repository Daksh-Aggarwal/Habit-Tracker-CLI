# 👁 Habit Tracker CLI

A simple, clean, and persistent command-line habit tracker built in Python.
Track your daily habits, build streaks, and never miss a goal again — all from your terminal.


## 🚀 Features

* ✅ Add new habits
* ✅ Mark habits as done (with streak logic)
* ✅ View all habits with current streaks and timestamps
* ✅ Edit and delete habits as required
* ✅ Data persistence using JSON
* ✅ Automatically prevents double-logging for the same day
* ✅ Clean, modular Python code — easy to maintain and extend


## 🖥️ How It Works

* Habits are stored in a local file: `habits.json` (On first run, a `habits.json` file will be created automatically)
* When you mark a habit as done:

  * If it was done yesterday → your streak increases
  * If you missed days → your streak resets
  * If you've already marked it today → it doesn't count again
* You can view all habits and their current streaks anytime
* You can edit and delete any habit anytime


## 📦 Requirements

* Python 3.7+

All libraries used are part of the Python standard library.


## 🛠️ Getting Started

```bash
git clone https://github.com/Daksh-Aggarwal/Habit-Tracker-CLI.git
cd Habit-Tracker-CLI
python habit_tracker.py
```


## 📸 Demo

```
1. Add Habit
2. Mark Habit as Done
3. View Habits and Streaks
4. Edit Habit
5. Delete Habit
6. Exit

What habit would you like to store? Drink Water
Successfully added new habit!

Which habit would you like to mark as done? 1
Habit marked done successfully! Your current streak is 1.
```


## 🧩 Folder Structure

```
habit-tracker-cli/
├── habit_tracker.py
├── habits.json  ← (auto-created)
└── README.md
```


## 🧠 Future Improvements

* Longest streak tracking
* Web version using Flask (in progress)


## 🡩‍💻 Author

Made with ❤️ by **Daksh Aggarwal**
[GitHub](https://github.com/Daksh-Aggarwal) • [LinkedIn](https://www.linkedin.com/in/dakshaggarwal7)

## 📄 License

This project is licensed under the MIT License.
