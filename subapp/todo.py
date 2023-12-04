import tkinter as tk
from tkinter import ttk, messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pretty Todo List")
        self.master.configure(bg="#BEE3F8") 

        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=30, font=("Courier", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=30, height=10, font=("Courier", 12))
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.delete_button = ttk.Button(master, text="Delete Task", command=self.delete_task, style="TButton")
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.complete_button = ttk.Button(master, text="Mark Complete", command=self.mark_complete, style="TButton")
        self.complete_button.grid(row=2, column=1, padx=10, pady=10)

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", font=("Courier", 12), background="#8FB4FF", foreground="black")
        self.style.configure("TEntry", font=("Courier", 12), background="#E2E2E2")
        self.style.configure("TListbox", font=("Courier", 12), background="#E2E2E2")

    def add_task(self):
        task_text = self.task_var.get()
        if task_text:
            self.tasks.append({"task": task_text, "complete": False})
            self.task_var.set("")
            self.populate_listbox()

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            complete = task["complete"]
            status = " [✔]" if complete else " [✘]"
            self.task_listbox.insert(tk.END, f"{task_text}{status}")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.populate_listbox()

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["complete"] = not self.tasks[index]["complete"]
            self.populate_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
