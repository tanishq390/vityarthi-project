#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanishq
#
# Created:     23-11-2025
# Copyright:   (c) Tanishq 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import json
import os
from datetime import datetime

DATA_FILE = "complaints.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
def file_complaint():
    data = load_data()

    complaint = {
        "id": len(data) + 1,
        "name": input("Enter your name: "),
        "roll": input("Enter your registration number: "),
        "department": input("Enter your department: "),
        "issue": input("Describe your complaint: "),
        "status": "Pending",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(complaint)
    save_data(data)
    print("\nComplaint filed successfully! Your complaint ID is:", complaint["id"])
def view_complaints():
    data = load_data()
    if not data:
        print("No complaints found.")
        return

    print("\n----------- All Complaints -----------")
    for c in data:
        print(f"""
Complaint ID : {c['id']}
Name         : {c['name']}
Roll No.     : {c['roll']}
Department   : {c['department']}
Issue        : {c['issue']}
Status       : {c['status']}
Date         : {c['date']}
--------------------------------------------
""")

def update_status():
    data = load_data()
    if not data:
        print("No complaints to update.")
        return
    cid = int(input("Enter Complaint ID to update: "))
    found = False
    for c in data:
        if c["id"] == cid:
            print("Current Status:", c["status"])
            new_status = input("Enter new status (Pending/In-Progress/Resolved): ")
            c["status"] = new_status
            found = True
            break

    if not found:
        print("Complaint ID not found!")
    else:
        save_data(data)
        print("Status updated successfully.")
while True:
    print("""
==============================
   College Complaint System
==============================

1. File a Complaint
2. View All Complaints (Admin)
3. Update Complaint Status (Admin)
4. Exit
""")
    choice = input("Enter your choice: ")
    if choice == "1":
        file_complaint()
    elif choice == "2":
        view_complaints()
    elif choice == "3":
        update_status()
    elif choice == "4":
        print("Exiting system...")
        break
    else:

        print("Invalid choice. Try again!")
