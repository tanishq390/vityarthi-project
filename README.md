📌 College Complaint Management System

A simple CLI-based system to file, view, and update college complaints using Python and JSON storage.


---

🚀 Features

File a Complaint
Students can submit complaints with basic details.

View All Complaints (Admin)
Shows every complaint stored in the system.

Update Complaint Status (Admin)
Change status to Pending, In-Progress, or Resolved.

Local JSON Storage
All complaints are saved in complaints.json.



---

🗂️ Project Structure

.
├── main.py
└── complaints.json   # generated automatically after first use


---

🛠️ How It Works

▶️ 1. File a Complaint

Collects:

Name

Registration number

Department

Issue description


Then stores the complaint with:

Auto-generated ID

Status = "Pending"

Timestamp


📜 2. View Complaints (Admin)

Displays:

ID

Name

Roll

Department

Issue

Status

Date


🔧 3. Update Complaint Status (Admin)

Updates complaint by ID.


---

📦 Prerequisites

You only need Python 3.x.
No external libraries required.


---

▶️ Run the Project

python main.py

The menu will appear:

1. File a Complaint
2. View All Complaints (Admin)
3. Update Complaint Status (Admin)
4. Exit


---

💾 Data Storage

All complaint records are saved inside complaints.json, generated automatically if missing.

Sample stored data:

{
  "id": 1,
  "name": "John Doe",
  "roll": "123456",
  "department": "CSE",
  "issue": "Network issue in lab",
  "status": "Pending",
  "date": "2025-02-20 15:40:10"
}


---

🧩 Code Overview

🔹 load_data()

Loads JSON file into Python list.

🔹 save_data(data)

Writes updated list back to JSON.

🔹 file_complaint()

Handles complaint submission.

🔹 view_complaints()

Prints all stored complaints.

🔹 update_status()

Changes complaint status by ID.

🔹 Main Loop

Displays menu and routes actions.


---

🛠️ Future Enhancements

Authentication for admin access

Search complaints by roll number

Export complaints to CSV/PDF

GUI or web-based dashboard

Auto-email confirmation# vityarthi-project
