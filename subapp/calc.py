import tkinter as tk
from tkinter import messagebox

class CuteCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Calculator")
        self.root.geometry("400x600")
        self.root.config(bg="#FFCCFF")  # Set background color

        # Entry widget to display the expression
        self.expression_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.expression_var, font=('Comic Sans MS', 24), bd=10, insertwidth=4, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons for digits and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, padx=20, pady=20, font=('Comic Sans MS', 14), command=lambda t=text: self.button_click(t), bg="#FF99CC").grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        current_expression = self.expression_var.get()

        try:
            if value == '=':
                result = str(eval(current_expression))
                self.expression_var.set(result)
            elif value == 'C':
                self.expression_var.set('')
            else:
                self.expression_var.set(current_expression + value)
        except Exception as e:
            self.expression_var.set("Error")
            messagebox.showerror("Error", "Invalid Expression")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CuteCalculator(root)
    root.mainloop()
