import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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

        # Add a cute image (replace "cute_image.png" with your own image)
        self.cute_image = tk.PhotoImage(file="cute_image.png")
        image_label = tk.Label(root, image=self.cute_image, bg=bg_color)
        image_label.pack()

        self.load_existing_note()

    def update_date_label(self):
        current_date = tk.StringVar()
        current_date.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        date_label = tk.Label(self.root, textvariable=current_date, bg="#FFDAB9", fg="#4B0082", font=("Comic Sans MS", 8))
        date_label.pack(side=tk.BOTTOM, pady=5)

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

