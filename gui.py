import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sys

# Import existing modules and functions
from main import is_valid_data_type, is_valid_symbol, is_valid_date, is_valid_interval, is_valid_format
from stocks import stock_prices
from crypto import crypto_prices
from currency import forex_rates
from utils import data

# Function to handle the submission


def on_submit():
    data_type = data_type_var.get()
    symbol = symbol_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    interval = interval_var.get()
    format = format_var.get()

    try:
        # Validate inputs
        if not is_valid_data_type(data_type) or not is_valid_symbol(symbol) or not is_valid_date(start_date) or not is_valid_date(end_date) or not is_valid_interval(interval) or not is_valid_format(format):
            raise ValueError("Invalid input")

        # Fetch and process data
        # ... [existing data fetching and processing logic] ...

        messagebox.showinfo(
            "Success", "Data processed and saved successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Set up the main application window
root = tk.Tk()
root.title("Financial Data Extractor")

# Variables for dropdowns
data_type_var = tk.StringVar(value='stocks')
interval_var = tk.StringVar(value='daily')
format_var = tk.StringVar(value='csv')

# Create and place widgets
tk.Label(root, text="Financial data type").pack()
tk.OptionMenu(root, data_type_var, 'stocks', 'crypto', 'forex').pack()

tk.Label(root, text="Symbol").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

tk.Label(root, text="Start date (YYYY-MM-DD)").pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

tk.Label(root, text="End date (YYYY-MM-DD)").pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

tk.Label(root, text="Interval").pack()
tk.OptionMenu(root, interval_var, '1min', '5min', '15min',
              '30min', '60min', 'daily', 'weekly', 'monthly').pack()

tk.Label(root, text="Format").pack()
tk.OptionMenu(root, format_var, 'xlsx', 'csv', 'json').pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
