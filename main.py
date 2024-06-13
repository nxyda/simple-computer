import random
import string
import datetime
import time
import calendar as cal_module
import os

list_of_commands = ["exit", "help", "calculator", "create document", "edit document", "open document", "delete document", "clock", "calendar"]

login = "admin"
password = "admin"

running = False

print("Enter login:")  
login_input = input()
if login_input == login:
    print("Enter password:")
    password_input = input()
    if password_input == password:
        print("Welcome!")
        running = True
    else:
        print("Password is incorrect")
else: 
    print("Login is incorrect")

def calculator():
    while True:  
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break  
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 1:
            print(num1 + num2)
        elif choice == 2:
            print(num1 - num2)  
        elif choice == 3:
            print(num1 * num2)  
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(num1 / num2)  
        else:
            print("Invalid choice")


def clock():
    while True:
        print("1. Show time")
        print("2. Stopwatch")
        print("3. Timer")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
        elif choice == 2:
            start_time = datetime.datetime.now()
            input("Press Enter to stop the stopwatch")
            end_time = datetime.datetime.now()
            print("Time elapsed: ", end_time - start_time)
        elif choice == 3:
            duration = int(input("Enter the duration of the timer in seconds: "))
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)
            while datetime.datetime.now() < end_time:
                time_left = end_time - datetime.datetime.now()
                print("Time left: ", time_left)
                time.sleep(1)
            print("Time's up!")
        elif choice == 4:
            break

events = {}  

def show_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print(cal_module.month(year, month))

def add_event():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    event = input("Enter event: ")
    if year not in events:
        events[year] = {}
    if month not in events[year]:
        events[year][month] = {}
    if day not in events[year][month]:
        events[year][month][day] = []
    events[year][month][day].append(event)
    print("Event added successfully!")

def remove_event():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    if year in events and month in events[year] and day in events[year][month]:
        event = input("Enter event to remove: ")
        if event in events[year][month][day]:
            events[year][month][day].remove(event)
            if not events[year][month][day]:
                del events[year][month][day]
            if not events[year][month]:
                del events[year][month]
            if not events[year]:
                del events[year]
            print("Event removed successfully!")
        else:
            print("Event not found.")
    else:
        print("No events on this date.")

def show_events():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    if year in events and month in events[year]:
        print("Events in", year, month, ":")
        for day in events[year][month]:
            for event in events[year][month][day]:
                print(f"  {day}: {event}")
    else:
        print("No events in this month.")

def calendar():
    while True:
        print("1. Show calendar")
        print("2. Add event")
        print("3. Remove event")
        print("4. Show events")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_calendar()
        elif choice == 2:
            add_event()
        elif choice == 3:
            remove_event()
        elif choice == 4:
            show_events()
        elif choice == 5:
            break

while running:    
    command = input("Enter command: ")
    if command == "exit":
        running = False
    elif command == "help":
        for i in list_of_commands:
            print(i)
    elif command == "calculator":
        calculator()
    elif command == "create document":
        print("Enter document name:")
        document_name = input()
        print("Enter document content:")
        document_content = input()
        with open(document_name, "w") as f:
            f.write(document_content)
        print("Document created successfully!")
    elif command == "edit document":
        print("Enter document name:")
        document_name = input()
        print("Enter new document content:")
        document_content = input()
        with open(document_name, "w") as f:
            f.write(document_content)
        print("Document edited successfully!")
    elif command == "open document":
        print("Enter document name:")
        document_name = input()
        with open(document_name, "r") as f:
            print(f.read())
    elif command == "delete document":
        print("Enter document name:")
        document_name = input()
        os.remove(document_name)
        print("Document deleted successfully!")
    elif command == "clock": 
        clock()
    elif command == "calendar":
        calendar()