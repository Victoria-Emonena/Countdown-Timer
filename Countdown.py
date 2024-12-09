import time
import os

# Function to alert user after time has elapsed
def play_sound():
    if os.name == "nt":
        import winsound
        winsound.Beep(1000, 500)
    else:
        print("\a")

# Function to convert input to seconds and display timer
def countdown(hours, minutes, seconds):
    t = hours * 3600 + minutes * 60 + seconds
    while t:
        hrs, rem = divmod(t, 3600)
        mins, secs = divmod(rem, 60)
        timer = "{:02d}:{:02d}:{:02d}".format(hrs, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("\nEnd of Timer!")
    play_sound()

# Function to get user input
def get_time_input():
    while True:
        try:
            # Prompt the user to enter time in "HH:MM:SS" format
            time_input = input("Enter time duration (HH:MM:SS): ")
            hours, minutes, seconds = map(int, time_input.split(":"))
            if seconds < 0 or minutes >= 60 or seconds >= 60:
                raise ValueError
            return hours, minutes, seconds
        except ValueError:
            print("Invalid input! Please enter the time in 'HH:MM:SS' format.")

# Calling functions to perform task
hours, minutes, seconds = get_time_input()
countdown(hours, minutes, seconds)
