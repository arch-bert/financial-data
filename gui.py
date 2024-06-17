import tkinter as tk

# Create & configure loading window
window = tk.Tk()
window.configure(bg="#222222", height=400, width=600)

# Create dropdown menu
options = ["Crypto", "Stocks", "Forex"]
selected_option = tk.StringVar(window)
selected_option.set(options[1])  # Default: Stocks

dropdown = tk.OptionMenu(window, selected_option, *options)
dropdown.configure(bg="#2b2b2b")  # Change dropdown background color
dropdown.pack()

if __name__ == "__main__":
    window.mainloop()