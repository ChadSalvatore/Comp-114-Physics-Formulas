import tkinter as tk
from tkinter import messagebox
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
        self.configure(bg="#8B0000") # dark red background
        self.resizable(False, False)

        self.font = ("Times New Roman", 12)
        self.title_font = ("Times New Roman", 16, "bold")

        self.create_main_menu()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_credits(self):
        """Add credit text at bottom left."""
        credit = tk.Label(
            self,
            text="Reden and Nisar, at BSEE 2B",
            font=("Times New Roman", 10, "italic"),
            fg="white",
            bg="#8B0000",
            anchor="w"
        )
        credit.place(x=10, y=405)

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self, text="Formula Calculator", font=self.title_font, fg="white", bg="#8B0000").pack(pady=25)

        self.make_button("Physics Formulas", self.physics_menu)
        self.make_button("Geometry Formulas", self.geometry_menu)
        self.make_button("Exit", self.destroy)

        self.add_credits()

    def make_button(self, text, command):
        """Uniform button style."""
        tk.Button(
            self,
            text=text,
            font=self.font,
            width=25,
            bg="#B22222",
            fg="white",
            activebackground="#FF6347",
            activeforeground="white",
            relief="flat",
            command=command
        ).pack(pady=10)

    def physics_menu(self):
        self.clear_frame()
        tk.Label(self, text="Physics Formulas", font=self.title_font, fg="white", bg="#8B0000").pack(pady=15)

        self.make_button("Speed (distance / time)", self.input_speed)
        self.make_button("Force (mass × acceleration)", self.input_force)
        self.make_button("Kinetic Energy (½mv²)", self.input_ke)
        self.make_button("Potential Energy (mgh)", self.input_pe)
        self.make_button("Back", self.create_main_menu)

        self.add_credits()

    def geometry_menu(self):
        self.clear_frame()
        tk.Label(self, text="Geometry Formulas", font=self.title_font, fg="white", bg="#8B0000").pack(pady=15)

        self.make_button("Area of Circle (πr²)", self.input_circle_area)
        self.make_button("Perimeter of Circle (2πr)", self.input_circle_perimeter)
        self.make_button("Area of Rectangle (L×W)", self.input_rectangle_area)
        self.make_button("Area of Triangle (½bh)", self.input_triangle_area)
        self.make_button("Back", self.create_main_menu)

        self.add_credits()

    def ask_inputs(self, fields, formula_func, formula_name, unit, back_menu):
        self.clear_frame()
        tk.Label(self, text=formula_name, font=self.title_font, fg="white", bg="#8B0000").pack(pady=10)

        entries = {}
        for label in fields:
            frame = tk.Frame(self, bg="#8B0000")
            frame.pack(pady=3)
            tk.Label(frame, text=f"{label}: ", font=self.font, bg="#8B0000", fg="white").pack(side=tk.LEFT)
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

        tk.Button(
            self, text="Calculate", font=self.font, width=15,
            bg="#B22222", fg="white", activebackground="#FF6347",
            activeforeground="white", relief="flat", command=calculate
        ).pack(pady=10)

        tk.Button(
            self, text="Back", font=self.font, width=15,
            bg="#B22222", fg="white", activebackground="#FF6347",
            activeforeground="white", relief="flat", command=back_menu
        ).pack()

        self.add_credits()

    # --- Input Screens ---
    def input_speed(self): self.ask_inputs(["Distance (m)", "Time (s)"], calc_speed, "Speed", "m/s", self.physics_menu)
    def input_force(self): self.ask_inputs(["Mass (kg)", "Acceleration (m/s²)"], calc_force, "Force", "N", self.physics_menu)
    def input_ke(self): self.ask_inputs(["Mass (kg)", "Velocity (m/s)"], calc_kinetic_energy, "Kinetic Energy", "J", self.physics_menu)
    def input_pe(self): self.ask_inputs(["Mass (kg)", "Height (m)"], calc_potential_energy, "Potential Energy", "J", self.physics_menu)
    def input_circle_area(self): self.ask_inputs(["Radius (m)"], calc_circle_area, "Area of Circle", "m²", self.geometry_menu)
    def input_circle_perimeter(self): self.ask_inputs(["Radius (m)"], calc_circle_perimeter, "Perimeter of Circle", "m", self.geometry_menu)
    def input_rectangle_area(self): self.ask_inputs(["Length (m)", "Width (m)"], calc_rectangle_area, "Area of Rectangle", "m²", self.geometry_menu)
    def input_triangle_area(self): self.ask_inputs(["Base (m)", "Height (m)"], calc_triangle_area, "Area of Triangle", "m²", self.geometry_menu)


# --- Run App ---
if __name__ == "__main__":
    app = FormulaApp()
    app.mainloop()