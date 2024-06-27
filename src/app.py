import tkinter as tk
import pyautogui
import time

class MousePositionLogger(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mouse Position Tracker")

        self.attributes('-topmost', True)

        self.time_label = tk.Label(self, text="Waiting time (seconds):")
        self.time_label.pack(pady=10)
        self.time_entry = tk.Entry(self)
        self.time_entry.pack()

        self.time_entry.insert(0, "5")

        self.instructions_label = tk.Label(self, text="Click button to get mouse position")
        self.instructions_label.pack(pady=5)

        self.get_position_button = tk.Button(self, text="Get Mouse Position", command=self.get_mouse_position)
        self.get_position_button.pack(pady=10)

        self.log_text = tk.Text(self, height=10, width=40)
        self.log_text.pack(padx=10, pady=10)

    def get_mouse_position(self):
        try:
            wait_time = float(self.time_entry.get())
        except ValueError:
            self.instructions_label.config(text="Invalid time. Use numbers.")
            return

        self.start_countdown(int(wait_time))

    def start_countdown(self, seconds):
        if seconds <= 0:
            self.capture_mouse_position()
        else:
            self.instructions_label.config(text=f"Capture in {seconds} seconds...")
            self.after(1000, lambda: self.start_countdown(seconds - 1))

    def capture_mouse_position(self):
        self.instructions_label.config(text="Capturing mouse position...")
        mouse_position = pyautogui.position()
        self.instructions_label.config(text=f"Mouse position: {mouse_position}")

        self.log_text.insert(tk.END, f"{mouse_position}\n")
        self.log_text.see(tk.END)  

        self.log_text.bind("<Button-1>", lambda event: self.log_text.focus_set())
        self.log_text.bind("<Control-a>", lambda event: self.log_text.tag_add(tk.SEL, "1.0", tk.END))
        self.log_text.bind("<Control-c>", lambda event: self.log_text.clipboard_clear())
        self.log_text.bind("<Control-c>", lambda event: self.log_text.clipboard_append(self.log_text.selection_get()), add="+")

if __name__ == "__main__":
    app = MousePositionLogger()
    app.mainloop()
