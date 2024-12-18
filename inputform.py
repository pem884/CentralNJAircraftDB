import tkinter as tk
from tkinter import messagebox
import csv
import re

def clear_fields():
     hex_entry.delete(0, tk.END)
     nnumber_entry.delete(0, tk.END)
     airport_entry.delete(0, tk.END)

def add_to_csv():
    hex_id = hex_entry.get()
    n_number = nnumber_entry.get()
    airport_base = airport_entry.get()

    # Strip non-alphanumeric characters from input fields
    hex_id = re.sub('[^A-Za-z0-9]+', '', hex_id)
    n_number = re.sub('[^A-Za-z0-9]+', '', n_number)
    airport_base = re.sub('[^A-Za-z0-9]+', '', airport_base)

    if not (hex_id and n_number and airport_base):
        messagebox.showwarning("Empty fields", "Please fill all the fields")
        return

    with open('data\\Lookup-NNumber-Airport.csv', 'r+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            if row == [hex_id, n_number, airport_base]:
                messagebox.showwarning("Duplicate entry", "This entry already exists.")
                return

        writer = csv.writer(file)
        writer.writerow([hex_id, n_number, airport_base])

    clear_fields()

root = tk.Tk()
root.title('Hex-NNumber-Airport input')

hex_label = tk.Label(root, text="Hex ID:")
hex_label.pack()

hex_entry = tk.Entry(root)
hex_entry.pack()

nnumber_label = tk.Label(root, text="N Number:")
nnumber_label.pack()

nnumber_entry = tk.Entry(root)
nnumber_entry.pack()

airport_label = tk.Label(root, text="Airport Base:")
airport_label.pack()

airport_entry = tk.Entry(root)
airport_entry.pack()

add_button = tk.Button(root, text="Add", command=add_to_csv)
add_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

root.mainloop()