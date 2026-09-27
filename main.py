import json

habits = {}
skipped = {}

def add_habits(name):
    habits[name] = []
    skipped[name] = []

def mark_done(habit_name, date):
    habits[habit_name].append(date)

def mark_missed(habit_name, date):
    skipped[habit_name].append(date)

def weekly_summary(habit_name):
    result = len(habits[habit_name])
    return result

while True:
    habit_name = input("Enter a habit name (or 'done' to stop adding habits): ")
    if habit_name == "done":
        break

    add_habits(habit_name)

    while True:
        done_date = input(f"Enter a date you completed '{habit_name}' (or 'done' to stop): ")
        if done_date == "done":
            break
        mark_done(habit_name, done_date)

    while True:
        missed_date = input(f"Enter a date you missed '{habit_name}' (or 'done' to stop): ")
        if missed_date == "done":
            break
        mark_missed(habit_name, missed_date)

data = {"habits": habits, "skipped": skipped}

with open("data.json", "w") as file:
    json.dump(data, file)

for habit_name in habits:
    total_days = len(habits[habit_name]) + len(skipped[habit_name])

    if total_days == 0:
        print(f"{habit_name}: no data entered.")
        continue

    output = (weekly_summary(habit_name) / total_days) * 100

    print(f"\n{habit_name}: {weekly_summary(habit_name)} out of {total_days} days")

    if output >= 80:
        print("Amazing consistency! Keep this momentum going.")
    elif 60 <= output < 80:
        print("Solid progress! A few more days and you'll be unstoppable.")
    else:
        print("It's okay, every day is a fresh start. You've got this.")