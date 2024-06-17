import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Financial Data Extractor")
        self.geometry("400x200")

        self.label = ctk.CTkLabel(self, text="Select Data Type")
        self.label.pack(pady=(20, 10))

        self.dropdown = ctk.CTkComboBox(self, values=["Crypto", "Stocks", "Forex"])
        self.dropdown.set("Stocks")
        self.dropdown.pack(pady=(0, 20))

        self.button = ctk.CTkButton(self, text="Confirm", command=self.on_confirm)
        self.button.pack()

    def on_confirm(self):
        selected = self.dropdown.get()
        print(f"Selected: {selected}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
