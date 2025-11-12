import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- Formula Functions ---
def calc_speed(distance, time): return distance / time
def calc_force(mass, acceleration): return mass * acceleration
def calc_kinetic_energy(mass, velocity): return 0.5 * mass * velocity ** 2
def calc_potential_energy(mass, height): return mass * 9.8 * height
def calc_circle_area(radius): return math.pi * radius ** 2
def calc_circle_perimeter(radius): return 2 * math.pi * radius
def calc_rectangle_area(length, width): return length * width
def calc_triangle_area(base, height): return 0.5 * base * height


# --- Main App ---
class FormulaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formula Calculator")
        self.geometry("420x430")
        self.resizable(False, False)

        # Set a uniform font
        self.font = ("Times New Roman", 12)
        self.title_font = ("Times New Roman", 16, "bold")

        self.create_main_menu()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_credits(self):
        """Adds credit text at the bottom left corner."""
        credit = tk.Label(
            self,
            text="Reden and Nisar, at BSEE 2B",
            font=("Times New Roman", 10, "italic"),
            anchor="w"
        )
        credit.place(x=10, y=405)

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self, text="Formula Calculator", font=self.title_font).pack(pady=25)

        tk.Button(self, text="Physics Formulas", font=self.font, width=25, command=self.physics_menu).pack(pady=10)
        tk.Button(self, text="Geometry Formulas", font=self.font, width=25, command=self.geometry_menu).pack(pady=10)
        tk.Button(self, text="Exit", font=self.font, width=25, command=self.destroy).pack(pady=20)

        self.add_credits()

    def physics_menu(self):
        self.clear_frame()
        tk.Label(self, text="Physics Formulas", font=self.title_font).pack(pady=15)

        tk.Button(self, text="Speed (distance / time)", font=self.font, width=30, command=self.input_speed).pack(pady=5)
        tk.Button(self, text="Force (mass × acceleration)", font=self.font, width=30, command=self.input_force).pack(pady=5)
        tk.Button(self, text="Kinetic Energy (½mv²)", font=self.font, width=30, command=self.input_ke).pack(pady=5)
        tk.Button(self, text="Potential Energy (mgh)", font=self.font, width=30, command=self.input_pe).pack(pady=5)
        tk.Button(self, text="Back", font=self.font, width=30, command=self.create_main_menu).pack(pady=15)

        self.add_credits()

    def geometry_menu(self):
        self.clear_frame()
        tk.Label(self, text="Geometry Formulas", font=self.title_font).pack(pady=15)

        tk.Button(self, text="Area of Circle (πr²)", font=self.font, width=30, command=self.input_circle_area).pack(pady=5)
        tk.Button(self, text="Perimeter of Circle (2πr)", font=self.font, width=30, command=self.input_circle_perimeter).pack(pady=5)
        tk.Button(self, text="Area of Rectangle (L×W)", font=self.font, width=30, command=self.input_rectangle_area).pack(pady=5)
        tk.Button(self, text="Area of Triangle (½bh)", font=self.font, width=30, command=self.input_triangle_area).pack(pady=5)
        tk.Button(self, text="Back", font=self.font, width=30, command=self.create_main_menu).pack(pady=15)

        self.add_credits()

    def ask_inputs(self, fields, formula_func, formula_name, unit, back_menu):
        self.clear_frame()
        tk.Label(self, text=formula_name, font=self.title_font).pack(pady=10)

        entries = {}
        for label in fields:
            frame = tk.Frame(self)
            frame.pack(pady=3)
            tk.Label(frame, text=f"{label}: ", font=self.font).pack(side=tk.LEFT)
            ent = tk.Entry(frame, font=self.font, width=15)
            ent.pack(side=tk.LEFT)
            entries[label] = ent

        def calculate():
            try:
                values = [float(entries[f].get()) for f in fields]
                result = formula_func(*values)
                messagebox.showinfo("Result", f"{formula_name}\n\nResult = {result:.2f} {unit}")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers!")

        tk.Button(self, text="Calculate", font=self.font, width=15, command=calculate).pack(pady=10)
        tk.Button(self, text="Back", font=self.font, width=15, command=back_menu).pack()

        self.add_credits()

    # --- Specific Input Screens ---
    def input_speed(self):
        self.ask_inputs(["Distance (m)", "Time (s)"], calc_speed, "Speed", "m/s", self.physics_menu)

    def input_force(self):
        self.ask_inputs(["Mass (kg)", "Acceleration (m/s²)"], calc_force, "Force", "N", self.physics_menu)

    def input_ke(self):
        self.ask_inputs(["Mass (kg)", "Velocity (m/s)"], calc_kinetic_energy, "Kinetic Energy", "J", self.physics_menu)

    def input_pe(self):
        self.ask_inputs(["Mass (kg)", "Height (m)"], calc_potential_energy, "Potential Energy", "J", self.physics_menu)

    def input_circle_area(self):
        self.ask_inputs(["Radius (m)"], calc_circle_area, "Area of Circle", "m²", self.geometry_menu)

    def input_circle_perimeter(self):
        self.ask_inputs(["Radius (m)"], calc_circle_perimeter, "Perimeter of Circle", "m", self.geometry_menu)

    def input_rectangle_area(self):
        self.ask_inputs(["Length (m)", "Width (m)"], calc_rectangle_area, "Area of Rectangle", "m²", self.geometry_menu)

    def input_triangle_area(self):
        self.ask_inputs(["Base (m)", "Height (m)"], calc_triangle_area, "Area of Triangle", "m²", self.geometry_menu)


# --- Run App ---
if __name__ == "__main__":
    app = FormulaApp()
    app.mainloop()