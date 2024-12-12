from tkinter import *
from tkinter import messagebox
import area


class Gui:
    def __init__(self, window):
        self.window = window
        self.window.title("Area Calculator")
        self.window.geometry("500x350")
        self.window.resizable(False, False)

        # Create menu bar
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)

        # Add "Help" menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Add "Exit" menu
        self.menu_bar.add_command(label="Exit", command=self.window.quit)

        # Title label
        self.title_label = Label(self.window, text="Area Calculator", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Shape selection dropdown
        self.frame_shape = Frame(self.window)
        self.label_shape = Label(self.frame_shape, text="Select Shape:")
        self.shape_var = StringVar(value="Circle")
        self.shape_dropdown = OptionMenu(self.frame_shape, self.shape_var, "Circle", "Square", "Rectangle", "Triangle", command=self.shape_selected)
        self.label_shape.pack(side="left", padx=10)
        self.shape_dropdown.pack(side="left", padx=10)
        self.frame_shape.pack(pady=10)

        # Input fields
        self.frame_inputs = Frame(self.window)
        self.label_first = Label(self.frame_inputs, text="Dimension 1:")
        self.entry_first = Entry(self.frame_inputs, width=20)
        self.label_second = Label(self.frame_inputs, text="Dimension 2:")
        self.entry_second = Entry(self.frame_inputs, width=20)
        self.label_first.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_first.grid(row=0, column=1, padx=10, pady=5)
        self.label_second.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_second.grid(row=1, column=1, padx=10, pady=5)
        self.frame_inputs.pack(pady=10)

        # Buttons
        self.frame_buttons = Frame(self.window)
        self.button_compute = Button(self.frame_buttons, text="COMPUTE", command=self.compute, width=12, bg="lightblue")
        self.button_clear = Button(self.frame_buttons, text="CLEAR", command=self.clear_all, width=12, bg="lightcoral")
        self.button_compute.pack(side="left", padx=10)
        self.button_clear.pack(side="left", padx=10)
        self.frame_buttons.pack(pady=10)

        # Results
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result, text="Result: ", font=("Arial", 12), fg="darkgreen")
        self.label_result.pack()
        self.frame_result.pack(pady=10)

    def shape_selected(self, selected_shape):
        # Reset inputs and labels
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text="Result: ")
        if selected_shape == "Circle":
            self.label_first.config(text="Radius:")
            self.label_second.grid_remove()
            self.entry_second.grid_remove()
        elif selected_shape == "Square":
            self.label_first.config(text="Side:")
            self.label_second.grid_remove()
            self.entry_second.grid_remove()
        elif selected_shape == "Rectangle":
            self.label_first.config(text="Length:")
            self.label_second.config(text="Width:")
            self.label_second.grid()
            self.entry_second.grid()
        elif selected_shape == "Triangle":
            self.label_first.config(text="Base:")
            self.label_second.config(text="Height:")
            self.label_second.grid()
            self.entry_second.grid()

    def compute(self):
        try:
            shape = self.shape_var.get()
            first_num = float(self.entry_first.get())
            second_num = self.entry_second.get()

            if shape == "Circle":
                result = area.circle(first_num)
            elif shape == "Square":
                result = area.square(first_num)
            elif shape == "Rectangle":
                result = area.rectangle(first_num, float(second_num))
            elif shape == "Triangle":
                result = area.triangle(first_num, float(second_num))
            else:
                result = "Invalid shape"

            self.label_result.config(text=f"Result: {result:.2f}")
        except ValueError:
            self.label_result.config(text="Error: Enter valid numeric values")
        except TypeError:
            self.label_result.config(text="Error: Values must be positive")

    def clear_all(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text="Result: ")

    def show_about(self):
        messagebox.showinfo("About", "Area Calculator\nVersion 1.0\nCreated for Lab 11")


