################ GUI PACKAGES ################

import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar

################ OWN PACKAGES ################

from utils import data
from datetime import datetime
# from stocks import stock_prices
# from crypto import crypto_prices
# from currency import forex_rates
from utils.suppress_print import SuppressPrint

################ CONFIGURE GUI ################

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x700")

################ main() FUNCTION ################


def main():
    # Create user input variables (String)
    data_type = ctk.StringVar()
    symbol = ctk.StringVar()
    start_date = ctk.StringVar()
    end_date = ctk.StringVar()
    interval = ctk.StringVar()
    format = ctk.StringVar()

    # Label for Data Type Dropdown Menu
    ctk.CTkLabel(root, text="Data Type:", font=('Helvetica', 10, 'bold')).grid(
        row=0, column=0, padx=10, pady=(10, 0), sticky='w')

    # Data Type Dropdown Menu
    data_type_options = ['stocks', 'crypto', 'forex']
    data_type.set('stocks')  # Set default value
    data_type_dropdown_menu = ctk.CTkOptionMenu(
        root, variable=data_type, values=data_type_options)
    data_type_dropdown_menu.grid(
        row=0, column=1, padx=10, pady=(10, 0), sticky='ew')

    # Label for Symbol Textbox
    ctk.CTkLabel(root, text="Symbol:", font=('Helvetica', 10, 'bold')).grid(
        row=1, column=0, padx=10, pady=10, sticky='w')

    # Symbol Textbox
    symbol_textbox = ctk.CTkEntry(root, textvariable=symbol)
    symbol_textbox.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    # Label for Start Date Button
    ctk.CTkLabel(root, text="Start Date:", font=('Helvetica', 10, 'bold')).grid(
        row=2, column=0, padx=10, pady=10, sticky='w')

    # Start Date Button
    ctk.CTkButton(root, text="Select Start Date",
                  command=lambda: open_calendar(start_date)).grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    # Label for End Date Button
    ctk.CTkLabel(root, text="End Date:", font=('Helvetica', 10, 'bold')).grid(
        row=3, column=0, padx=10, pady=10, sticky='w')

    # End Date Button
    ctk.CTkButton(root, text="Select End Date",
                  command=lambda: open_calendar(end_date)).grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    # Label for Interval Dropdown Menu
    ctk.CTkLabel(root, text="Interval:", font=('Helvetica', 10, 'bold')).grid(
        row=4, column=0, padx=10, pady=10, sticky='w')

    # Interval Dropdown Menu
    interval_options = ['1min', '5min', '15min', '30min',
                        '60min', 'daily', 'weekly', 'monthly']
    interval_dropdown_menu = ctk.CTkOptionMenu(root,
                                               variable=interval,
                                               values=interval_options)
    interval_dropdown_menu.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    # Label for Format Dropdown Menu
    ctk.CTkLabel(root, text="Format:", font=('Helvetica', 10, 'bold')).grid(
        row=5, column=0, padx=10, pady=10, sticky='w')

    # Format Dropdown Menu
    format_options = ['xlsx', 'csv', 'json']
    format_dropdown_menu = ctk.CTkOptionMenu(root,
                                             variable=format,
                                             values=format_options)
    format_dropdown_menu.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

    root.grid_columnconfigure(1, weight=1)

################ MY FUNCTIONS ################


def open_calendar(date_var):
    def set_date():
        date_var.set(cal.selection_get().strftime('%Y-%m-%d'))
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day', year=2024, month=1, day=23)
    cal.pack(fill="both", expand=True)
    tk.Button(top, text="OK", command=set_date).pack()


################ CALL main() ################

if __name__ == "__main__":
    main()
    root.mainloop()
