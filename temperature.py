
import tkinter as tk
from tkinter import ttk

def convert_temperature():
    def perform_conversion():
        try:
            # Get the temperature value from the entry widget
            input_temp = float(entry.get())

            # Check the selected input and output units
            input_unit = input_unit_var.get()
            output_unit = output_unit_var.get()

            # Perform the conversion
            if input_unit == "Celsius" and output_unit == "Fahrenheit":
                result = (input_temp * 9/5) + 32
            elif input_unit == "Celsius" and output_unit == "Kelvin":
                result = input_temp + 273.15
            elif input_unit == "Fahrenheit" and output_unit == "Celsius":
                result = (input_temp - 32) * 5/9
            elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
                result = (input_temp - 32) * 5/9 + 273.15
            elif input_unit == "Kelvin" and output_unit == "Celsius":
                result = input_temp - 273.15
            elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
                result = (input_temp - 273.15) * 9/5 + 32
            else:
                result = input_temp  # If same units are selected

            output_label.config(text=f"Converted: {result:.2f} {output_unit}")
        except ValueError:
            output_label.config(text="Invalid input. Enter a numeric value.")

    # Create the conversion window
    conversion_window = tk.Toplevel()
    conversion_window.title("Temperature Conversion")
    conversion_window.geometry("500x500")

    # Temperature input
    tk.Label(conversion_window, text="Enter Temperature:").pack()
    entry = tk.Entry(conversion_window)
    entry.pack()

    # Unit options
    unit_options = ["Celsius", "Fahrenheit", "Kelvin"]

    # Input unit selection
    tk.Label(conversion_window, text="Select Input Unit:").pack()
    input_unit_var = tk.StringVar()
    input_unit_menu = ttk.Combobox(conversion_window, textvariable=input_unit_var, values=unit_options)
    input_unit_menu.pack()

    # Output unit selection
    tk.Label(conversion_window, text="Select Output Unit:").pack()
    output_unit_var = tk.StringVar()
    output_unit_menu = ttk.Combobox(conversion_window, textvariable=output_unit_var, values=unit_options)
    output_unit_menu.pack()

    # Convert button in the conversion window
    convert_button = tk.Button(conversion_window, text="Convert", command=perform_conversion)
    convert_button.pack()

    # Output label in the conversion window
    output_label = tk.Label(conversion_window, text="")
    output_label.pack()

if __name__ == "__main__":
    # If this script is run directly, open the conversion window
    convert_temperature()