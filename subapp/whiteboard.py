import tkinter as tk
from tkinter import filedialog, messagebox

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
