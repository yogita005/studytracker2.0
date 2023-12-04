import math
from datetime import datetime
import random
from tkinter import *
from tkinter import Tk, Label, Entry, Button, Text, messagebox
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, messagebox
from tkinter import filedialog, messagebox

# ---------------------------- CONSTANTS ------------------------------- #
NPUR = "#B1B2FF"
NRED = "#B0578D"
PURPLE = "#BFA2DB"
PINK = "#F8E8EE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- Quotes ------------------------------- # 

quote=['Believe you can and you are halfway there.',
       'Success is not final, failure is not fatal: It is the courage to continue that counts.',
       'The only limit to our realization of tomorrow will be our doubts of today.',
       'It always seems impossible until it is done.']
quotess = random.choice(quote)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label_checkmark.config(text="")
    my_label_timer.config(text="Timer", fg=PURPLE)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        my_label_timer.config(text="Long Break", fg=NPUR)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        my_label_timer.config(text="Short Break", fg=NPUR)
        count_down(short_break_sec)
    else:
        my_label_timer.config(text="Working Time", fg=NRED)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        my_label_checkmark.config(text=marks)

# ---------------------------- todo ------------------------------- #         

def todo_timer():

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

# ---------------------------- notes ------------------------------- #         

def notes():
    class StickyNote:
        def __init__(self, root, note_id):
            self.root = root
            self.note_id = note_id
            self.root.title(f"Sticky Note {self.note_id}")

            # Customize colors and fonts
            bg_color = "#FFDAB9"  # PeachPuff color
            text_color = "#4B0082"  # Indigo color
            font_style = "Comic Sans MS"

            self.note_text = tk.Text(root, wrap=tk.WORD, height=10, width=30, bg=bg_color, fg=text_color, font=(font_style, 12))
            self.note_text.pack(padx=10, pady=10)

            self.editable_var = tk.BooleanVar(value=True)
            editable_checkbutton = tk.Checkbutton(root, text="Editable", variable=self.editable_var, bg=bg_color, fg=text_color, font=(font_style, 10))
            editable_checkbutton.pack(side=tk.LEFT, padx=5)

            open_button = tk.Button(root, text="Open", command=self.open_note, bg="#FF69B4", fg="white", font=(font_style, 10))
            open_button.pack(side=tk.LEFT, padx=5)

            save_button = tk.Button(root, text="Save", command=self.save_note, bg="#77DD77", fg="white", font=(font_style, 10))
            save_button.pack(side=tk.LEFT, padx=5)

            close_button = tk.Button(root, text="Close", command=self.close_note, bg="#FF4500", fg="white", font=(font_style, 10))
            close_button.pack(side=tk.RIGHT, padx=5)

            self.update_date_label()
            self.load_existing_note()

        def load_existing_note(self):
            try:
                with open(f"notes{self.note_id}.txt", "r") as file:
                    content = file.read()
                    self.note_text.insert(tk.END, content)
            except FileNotFoundError:
                pass

        def save_note(self):
            note_content = self.note_text.get("1.0", tk.END).strip()
            if note_content:
                with open(f"notes{self.note_id}.txt", "w") as file:
                    file.write(note_content)
                messagebox.showinfo("Sticky Note", "Note saved successfully.")
            else:
                messagebox.showwarning("Sticky Note", "Note is empty. Nothing to save.")
            self.update_date_label()

        def open_note(self):
            try:
                with open(f"notes{self.note_id}.txt", "r") as file:
                    content = file.read()
                    self.note_text.delete("1.0", tk.END)
                    self.note_text.insert(tk.END, content)
            except FileNotFoundError:
                messagebox.showwarning("Sticky Note", "No existing note found.")

        def close_note(self):
            self.root.destroy()


    class NoteListApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Note List")

            self.note_instances = []

            add_note_button = tk.Button(root, text="Add Note", command=self.add_note, bg="#FF69B4", fg="white", font=("Comic Sans MS", 12))
            add_note_button.pack(side=tk.TOP, pady=10)

        def add_note_instance(self, note_id):
            new_note = tk.Toplevel(self.root)
            StickyNote(new_note, note_id)
            self.note_instances.append(new_note)

        def add_note(self):
            new_note_id = len(self.note_instances) + 1
            self.add_note_instance(new_note_id)

    if __name__ == "__main__":
        root = tk.Tk()
        note_list_app = NoteListApp(root)

        root.mainloop()


# ---------------------------- whiteboard------------------------------- #

def whiteboard():
    class PaintApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Paint App")

            self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
            self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

            self.setup_menu()

            # Set up drawing variables
            self.draw_color = "black"
            self.line_width = 2
            self.old_x = None
            self.old_y = None

            # Bind mouse events
            self.canvas.bind("<B1-Motion>", self.paint)
            self.canvas.bind("<ButtonRelease-1>", self.reset)

        def setup_menu(self):
            menu_bar = tk.Menu(self.root)

            color_menu = tk.Menu(menu_bar, tearoff=0)
            color_menu.add_command(label="Black", command=lambda: self.set_color("black"))
            color_menu.add_command(label="Red", command=lambda: self.set_color("red"))
            color_menu.add_command(label="Blue", command=lambda: self.set_color("blue"))
            color_menu.add_command(label="Green", command=lambda: self.set_color("green"))
            color_menu.add_command(label="Yellow", command=lambda: self.set_color("yellow"))

            menu_bar.add_cascade(label="Colors", menu=color_menu)

            # Add eraser option
            menu_bar.add_command(label="Eraser", command=lambda: self.set_color("white"))

            # Add save option
            menu_bar.add_command(label="Save", command=self.save_canvas)

            self.root.config(menu=menu_bar)

        def set_color(self, new_color):
            self.draw_color = new_color

        def paint(self, event):
            x, y = event.x, event.y
            if self.old_x and self.old_y:
                self.canvas.create_line(self.old_x, self.old_y, x, y, width=self.line_width, fill=self.draw_color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
            self.old_x = x
            self.old_y = y

        def reset(self, event):
            self.old_x = None
            self.old_y = None

        def save_canvas(self):
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.canvas.postscript(file=file_path, colormode="color")
                messagebox.showinfo("Save", "Canvas saved successfully.")

    if __name__ == "__main__":
        root = tk.Tk()
        app = PaintApp(root)
        root.mainloop()

# ---------------------------- calculator ------------------------------- # 
        
def calc():

    class PastelCalculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Pastel Calculator")
            self.root.geometry("400x600")
            self.root.config(bg="#F0D9FF")
            
            # Entry widget to display the expression
            self.expression_var = tk.StringVar()
            entry = tk.Entry(root, textvariable=self.expression_var, font=('Courier', 24), bd=10, insertwidth=4, width=14, justify='right')
            entry.grid(row=0, column=0, columnspan=4, pady=10)

            # Buttons for digits and operators
            buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
            ]

            for (text, row, col) in buttons:
                button = tk.Button(root, text=text, width=5, height=2, font=('Courier', 14, 'bold'), command=lambda t=text: self.button_click(t), bg="#F1EAFF", fg="#87CEEB", bd=5, relief=tk.RAISED, borderwidth=5, padx=5, pady=5, highlightthickness=0, highlightbackground="#F8F8FF", highlightcolor="#F8F8FF")
                button.grid(row=row, column=col, padx=5, pady=5)

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

        def make_button_click_handler(self, value):
            
            for (text, row, col) in buttons:
                button = tk.Button(root, text=text, width=5, height=2, font=('Courier', 14, 'bold'), command=self.make_button_click_handler(text), bg="#F1EAFF", fg="#87CEEB", bd=5, relief=tk.RAISED, borderwidth=5, padx=5, pady=5, highlightthickness=0, highlightbackground="#F8F8FF", highlightcolor="#F8F8FF")
                button.grid(row=row, column=col, padx=5, pady=5)


    if __name__ == "__main__":
        root = tk.Tk()
        calculator = PastelCalculator(root)
        root.mainloop()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Study Tracker")
window.config(padx=100, pady=50, bg=PINK)

my_label_timer = Label(text="Timer", font=("Courier", 50), fg=NPUR, bg=PINK)
my_label_timer.grid(column=1, row=0)


my_label_quotes = Label(text=quotess, font=("Courier", 15), fg="#1F4172", bg=PINK)
my_label_quotes.grid(column=1, row=1)

my_label_checkmark = Label(fg=NRED, bg=PINK, font=("Arial", 20))
my_label_checkmark.grid(column=1, row=2)

button_start = Button(text="Start", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12), command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12),command=reset_timer)
button_reset.grid(column=2, row=3)

button_todo = Button(text="Todo", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12), command=todo_timer)
button_todo.grid(column=1, row=3)

button_flash = Button(text="whiteboard", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12), command=whiteboard)
button_flash.grid(column=2, row=5)

button_notes = Button(text="notes", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12), command=notes)
button_notes.grid(column=0, row=5)

button_calc = Button(text="calculator", highlightthickness=0,bg=NPUR, height=3, width= 10,font=(FONT_NAME, 12), command=calc)
button_calc.grid(column=1, row=5)

canvas = Canvas(width=300, height=300, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file='froggo.png')

canvas.create_image(100, 102, image=tomato_img)
timer_text = canvas.create_text(100, 150, text="00:00", fill="#EC53B0", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()
