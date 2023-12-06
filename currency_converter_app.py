import tkinter as tk
from tkinter import ttk
import requests

API_KEY = '906761c07e882831845487e3'
BASE_CURRENCY = 'INR'

def currency_converter_a():
    def convert_currency(amount, to_currency):
        # Perform currency conversion using ExchangeRate-API
        api_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
        params = {'apikey': API_KEY}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            exchange_rates = response.json().get('conversion_rates', {})
            conversion_rate = exchange_rates.get(to_currency)
            if conversion_rate is not None:
                converted_amount = amount * conversion_rate
                return converted_amount
            else:
                return None  # Unable to find conversion rate for the specified currency
        else:
            return None  # Error fetching exchange rates

    def perform_currency_conversion():
        try:
            amount = float(amount_entry.get())
            to_currency = to_currency_var.get().upper()

            converted_amount = convert_currency(amount, to_currency)
            if converted_amount is not None:
                converted_currency_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
            else:
                converted_currency_label.config(text="Invalid currency or error fetching exchange rates.")
        except ValueError:
            converted_currency_label.config(text="Invalid input. Please enter a valid number.")

    # Create the main window for currency conversion
    currency_window = tk.Tk()
    currency_window.geometry("500x500")
    currency_window.title("Currency Conversion")
    currency_window.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    currency_window.tk.call("set_theme", "dark")

    # Add widgets for currency conversion in the main window
    label = tk.Label(currency_window, text="Currency Conversion", font=('Arial', 16))
    label.pack(pady=10)

    amount_label = tk.Label(currency_window, text="Enter Amount:")
    amount_label.pack()

    amount_entry = ttk.Entry(currency_window)
    amount_entry.pack()

    to_currency_label = tk.Label(currency_window, text="To Currency:")
    to_currency_label.pack()

    # Option menu for selecting the currency to convert to
    currencies = ["USD", "EUR", "GBP", "JPY"]  # Add more currencies as needed
    to_currency_var = tk.StringVar(currency_window)
    to_currency_var.set(currencies[0])  # Set the default currency
    to_currency_menu = ttk.Combobox(currency_window, textvariable=to_currency_var, values=currencies)
    to_currency_menu.pack()

    convert_button = ttk.Button(currency_window, text="Convert", command=perform_currency_conversion)
    convert_button.pack()

    converted_currency_label = tk.Label(currency_window, text="Converted Amount:")
    converted_currency_label.pack()

    currency_window.mainloop()

if __name__ == "__main__":
    currency_converter_a()
