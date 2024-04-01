import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")

        self.label = tk.Label(self.root, text="Enter time in seconds:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.timer_label = tk.Label(self.root, text="")
        self.timer_label.pack(pady=10)

        self.time_remaining = 0
        self.timer_running = False

    def start_timer(self):
        try:
            self.time_remaining = int(self.entry.get())
            if self.time_remaining <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a positive integer.")
                return
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.timer_running = True
            self.update_timer()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.timer_running = False

    def update_timer(self):
        if self.timer_running and self.time_remaining > 0:
            self.timer_label.config(text=f"Time Remaining: {self.time_remaining} seconds")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_remaining == 0:
            self.timer_label.config(text="Time's up!")
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
