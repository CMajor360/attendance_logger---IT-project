import csv
from datetime import datetime

FILE_NAME = "attendance_records.csv"

print("Program started...")

def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "ID", "Status", "Date", "Time"])
    except FileExistsError:
        pass

def log_attendance():
    name = input("Enter personnel name: ").strip().title()
    personnel_id = input("Enter personnel ID: ").strip()
    status = input("Enter status (Present/Absent): ").strip().capitalize()

    if status not in ("Present", "Absent"):
        print("Invalid status. Input 'Present' or 'Absent'")
    
    now = datetime.now()
    date = now.strftime("%D-%M-%Y")
    time = now.strftime("%H:%M:%S")

    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, personnel_id, status, date, time])

        print(f"Attendance for {name}, {status} on {date} at {time} marked successfully!")

        if __name__ == "__main__":
            initialize_file()

def view_records():
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            print("\n===Attendance Records===")
            records_found = False
            for row in reader:
                print(f"Name:{row[0]}, ID:{row[1]}, Status:{row[2]}, Date:{row[3]}, Time:{row[4]}")
                records_found = True
            if not records_found:
                print("No attendance records found.")
            print()
    except FileExistsError:
        print("No records yet. Run program and log at least one attendance!")

def search_records():
    keyword = input("Enter name or date (DD/MM/YYYY): ").strip()
    found = False
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)
            print("\n===Search Results===")
            for row in reader:
                if keyword.lower() in row[0].lower() or keyword == row[3]:
                    print(f"Name: {row[0]}, ID: {row[1]}, Status: {row[2]}, Date: {row[3]}, Time: {row[4]}")
                    found = True
            if not found:
                print("No matching records found!")
    except FileExistsError:
        print("No records yet!")

def main():
    while True:
        print("\n===Personal Attendance Logger===")
        print("1. Log Attendance")
        print("2. View Records")
        print("3. Search Records")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            log_attendance()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_records()
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
            