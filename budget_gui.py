import csv
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

FILENAME = "transactions.csv"

def save_transaction():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if not date or not category or not amount:
        messagebox.showwarning("Missing Info", "All fields are required.")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    messagebox.showinfo("Saved", "Transaction saved.")
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def show_summary():
    if not os.path.exists(FILENAME):
        messagebox.showinfo("No Data", "No transactions saved yet.")
        return

    total = 0
    output_area.delete(1.0, tk.END)

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                date, category, amount = row
                output_area.insert(tk.END, f"{date} - {category}: £{amount}\n")
                try:
                    total += float(amount)
                except ValueError:
                    continue

    output_area.insert(tk.END, f"\nTotal Balance: £{total:.2f}")

# GUI Setup
root = tk.Tk()
root.title("Budget Tracker")

# Input Labels and Entries
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0, sticky="e")
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Amount (£):").grid(row=2, column=0, sticky="e")
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Save Transaction", command=save_transaction).grid(row=3, column=0, pady=10)
tk.Button(root, text="Show Summary", command=show_summary).grid(row=3, column=1)

# Output area
output_area = scrolledtext.ScrolledText(root, width=40, height=10)
output_area.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
