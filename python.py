import tkinter as tk
from tkinter import ttk
from time_1 import time
from conversion import conversion
from currency_converter_app import currency_converter_a
from temperature import convert_temperature 

root = tk.Tk()
root.geometry("500x500")
root.title("UNIT CONVERTER TOOL")

# Load the custom theme
root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
root.tk.call("set_theme", "dark")

label = tk.Label(root, text="THIS IS A TOOL TO CONVERT UNITS", font=('Arial', 18))
label.grid( column=0, columnspan=2, padx=40, pady=40)

# Set a fixed width and external padding for all buttons
button_style = {'style': 'Accent.TButton', 'padding': 20, 'width': 20,}

button1 = ttk.Button(root, text='UNIT CONVERSION', **button_style, command=conversion)
button1.grid(row=1,  pady=(0, 10))

button2 = ttk.Button(root, text='TIME CONVERSION', **button_style, command=time)
button2.grid(row=2,  pady=(0, 10))

button3 = ttk.Button(root, text='CURRENCY CONVERSION', **button_style, command=currency_converter_a)
button3.grid(row=3, pady=(0, 10))

button4 = ttk.Button(root, text='TEMPERATURE CONVERSION', **button_style, command=convert_temperature)
button4.grid(row=4,)
def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Remember, you have to use ttk widgets
button = ttk.Button(root, text="Change theme!", command=change_theme)
button.grid(row=10, pady=10)

close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.grid( pady=10)

root.mainloop()