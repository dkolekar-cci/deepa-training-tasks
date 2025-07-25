import datetime

def set_reminder(task, time_str):

    try:
        current_date = datetime.datetime.now().date()
        time_parts = time_str.split(":")

        if len(time_parts) != 2:
            return "Invalid time format. Use HH:MM."
        
        hour, minute = time_parts
        if not hour.isdigit() or not minute.isdigit():
            return "Hour and minute should be numbers."
        
        hour = int(hour)
        minute = int(minute)
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            return "Invalid time. Hour should be 0–23 and minute 0–59."
        return f"Reminder set for '{task}' at {hour:02d}:{minute:02d} on {current_date}"
    
    except Exception as e:
        return f"Something went wrong, Please try again: {e}"

task_input = input("Task: ")
time_input = input("Time (HH:MM): ")
message = set_reminder(task_input, time_input)
print(message)