import tkinter as tk
from tkinter import ttk
import datetime as dt
import pytz


def time():
    top = tk.Toplevel()
    top.title("Time Conversion")
    top.geometry("500x500")

    current_datetime = dt.datetime.now()
    current_datetime = current_datetime.replace(second=0, microsecond=0)  # Set seconds to zero
    current_datetime_1=current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    label = tk.Label(top, text="Enter time conversion details:" ,font=('Arial', 15))

    label.pack(pady=10)
    label_2= tk.Label(top, text="The current date and time is: " + current_datetime_1 ,font=('Arial', 15))
    label_2.pack()

    # Add more widgets for time conversion as needed

    timezones = [
        "America/New_York", 
        "Europe/London", 
        "Asia/Tokyo", 
        "Africa/Cairo", 
        "Australia/Sydney", 
        "Asia/Dubai", 
        "America/Los_Angeles",
        "Europe/Berlin",
        "Asia/Shanghai",
        "America/Toronto"
    ]

    # Dropdown menu for selecting a country
    country_label = tk.Label(top, text="Select a country:", font=('Arial', 15))
    country_label.pack(pady=5)

    selected_timezone = tk.StringVar()
    country_dropdown = ttk.Combobox(top, textvariable=selected_timezone, values=timezones)
    country_dropdown.pack(pady=10)
    country_dropdown.set(timezones[0])  # Set default value

    convert_button = ttk.Button(top, text="Convert", command=lambda: label_timezone.config(
    text=f"The current time in {selected_timezone.get()} is: {current_datetime.astimezone(pytz.timezone(selected_timezone.get())).strftime('%Y-%m-%d %H:%M:%S')}"))
    convert_button.pack(pady=10)

    label_timezone = tk.Label(top, text="", font=('Arial', 15))
    label_timezone.pack()


    close_button = ttk.Button(top, text="Close", command=top.destroy)
    close_button.pack(side=tk.BOTTOM, pady=10, anchor=tk.S)