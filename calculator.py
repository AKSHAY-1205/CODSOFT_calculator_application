import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.first_number_entry = tk.Entry(root, width=15)
        self.first_number_entry.grid(row=0, column=1, pady=5)

        self.second_number_entry = tk.Entry(root, width=15)
        self.second_number_entry.grid(row=1, column=1, pady=5)

        self.operation_var = tk.StringVar(value="Select Operation")
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "Add", "Subtract", "Multiply", "Divide")
        self.operation_menu.grid(row=2, column=1, pady=5)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=1, pady=5)

        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=4, column=1, pady=5)

        tk.Label(root, text="First Number:").grid(row=0, column=0, pady=5)
        tk.Label(root, text="Second Number:").grid(row=1, column=0, pady=5)
        tk.Label(root, text="Operation:").grid(row=2, column=0, pady=5)

    def calculate(self):
        try:
            num1 = float(self.first_number_entry.get())
            num2 = float(self.second_number_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
            else:
                messagebox.showerror("Error", "Please select a valid operation")
                return

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
