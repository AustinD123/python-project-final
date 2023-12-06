import tkinter as tk
from tkinter import ttk

# List of all types of units and the units in them
units = {
    "volume": {
        # To ad a new unit, put `"new_unit": {value}`
        # convert 1 cubic meter to the new unit and use that as the value
        # for example 1 cubic centimeter is 1000 litres
        "litres": 1000,
        "cubic meters": 1,
        "gallons": 264.172,
    },
    "length": {
        # m is taken as the standard value
        "mm": 0.001, 
        "m": 1, 
        "cm": 0.01,
        "km": 1000,
        "inch": 39.3701,
        "feet": 3.280841666667,
    },
    "mass": {
        # gram is taken as the standard value
        "kg": 1000,
        "gram": 1,
        "pound": 0.00220462,
    }
}

def converter(unit_type):
    top = tk.Toplevel()
    top.title(f"Unit conversion - {unit_type}")
    top.geometry("500x500")

   
    # Text
    label_1= tk.Label(top, text=f"Write the input {unit_type}",font=('Arial', 15),)
    label_1.pack()
    
    # Input value
    entry= tk.Entry(top, width= 40)
    entry.config(highlightbackground="GREY")
    entry.pack()

    unit = list(units[unit_type].keys())


    # Unit 1 drop down
    selected_unit = tk.StringVar()
    unit1_dropdown = ttk.Combobox(top, textvariable=selected_unit, values=list(units[unit_type].keys()))
    unit1_dropdown.pack(pady=10)
    unit1_dropdown.set(list(units[unit_type].keys())[0])  # Set default value


    # Unit 2 drop down
    required_unit = tk.StringVar()
    unit2_dropdown = ttk.Combobox(top, textvariable=required_unit, values=list(units[unit_type].keys()))
    unit2_dropdown.pack(pady=10)
    unit2_dropdown.set(list(units[unit_type].keys())[0])  # Set default value


    # convert button action
    convert_button = ttk.Button(top, text="Convert", command=lambda: label_answer.config(
        text=f"answer: {int(entry.get())/units[unit_type][required_unit.get()]*units[unit_type][selected_unit.get()]}",
    ))
    convert_button.pack(pady=10)

    # Answer text
    label_answer = tk.Label(top, text="", font=('Arial', 15))
    label_answer.pack()


    # Close button
    close_button = ttk.Button(top, text="Close", command=top.destroy)
    close_button.pack(side=tk.BOTTOM, pady=10, anchor=tk.S)


def conversion():
    top = tk.Toplevel()
    top.title("Unit Conversion")
    top.geometry("500x500")
    button_style = {'style': 'Accent.TButton', 'padding': 20, 'width': 20,}

    label = tk.Label(top, text="SELECT THE TYPE OF CONVERSION", font=('Arial', 18))
    label.grid( column=0, columnspan=2, padx=40, pady=40)


    # types of unit conversion (volume, mass, length)


    button1 = ttk.Button(top, text=f'VOLUME CONVERSION', **button_style, command= lambda: converter("volume"))
    button1.grid(row=1, pady=(0, 10))

    button2 = ttk.Button(top, text=f'MASS CONVERSION', **button_style, command= lambda: converter("mass"))
    button2.grid(row=2, pady=(0, 10))

    button3 = ttk.Button(top, text=f'LENGTH CONVERSION', **button_style, command= lambda: converter("length"))
    button3.grid(row=3, pady=(0, 10))
    # Close button
    close_button = ttk.Button(top, text="Close", command=top.destroy)
    close_button.grid( pady=10)
        




