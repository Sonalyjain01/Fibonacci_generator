import tkinter as tk
from tkinter import messagebox

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Generator")

        self.label = tk.Label(root, text="Fibonacci Generator", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.entry_label = tk.Label(root, text="Enter number of terms:", font=("Helvetica", 14))
        self.entry_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_sequence)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def generate_sequence(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError("The number must be greater than zero.")
            sequence = fibonacci_sequence(n)
            self.result_label.config(text=" ".join(map(str, sequence)))
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()
