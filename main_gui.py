import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Data not available."

def show_animals():
    messagebox.showinfo("Protected Animals", read_file("animals.txt"))

def show_threats():
    messagebox.showinfo("Threats to Animals", read_file("threats.txt"))

def show_guidelines():
    messagebox.showinfo("Protection Guidelines", read_file("guidelines.txt"))

def report_animal():
    report = report_entry.get()
    if report.strip() == "":
        messagebox.showwarning("Warning", "Please enter report details")
        return

    with open("reports.txt", "a") as f:
        f.write(f"{datetime.now()} - {report}\n")

    messagebox.showinfo("Success", "Animal report submitted successfully")
    report_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Animal Protection Awareness System")
root.geometry("400x400")

tk.Label(root, text="Animal Protection Awareness System",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="View Protected Animals",
          command=show_animals, width=30).pack(pady=5)

tk.Button(root, text="View Threats",
          command=show_threats, width=30).pack(pady=5)

tk.Button(root, text="Protection Guidelines",
          command=show_guidelines, width=30).pack(pady=5)

tk.Label(root, text="Report Injured Animal:").pack(pady=10)
report_entry = tk.Entry(root, width=40)
report_entry.pack(pady=5)

tk.Button(root, text="Submit Report",
          command=report_animal, width=30).pack(pady=10)

tk.Button(root, text="Exit",
          command=root.quit, width=30).pack(pady=10)

root.mainloop()
