import tkinter as tk
import pyautogui
import time

class MousePositionLogger(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mouse Position Tracker")

        self.attributes('-topmost', True)

        self.time_label = tk.Label(self, text="Tempo de espera (segundos):")
        self.time_label.pack(pady=10)
        self.time_entry = tk.Entry(self)
        self.time_entry.pack()

        self.time_entry.insert(0, "5")

        self.instructions_label = tk.Label(self, text="Clique no botão para obter a posição do mouse")
        self.instructions_label.pack(pady=5)

        self.get_position_button = tk.Button(self, text="Obter Posição do Mouse", command=self.get_mouse_position)
        self.get_position_button.pack(pady=10)

        self.log_text = tk.Text(self, height=10, width=40)
        self.log_text.pack(padx=10, pady=10)

    def get_mouse_position(self):
        try:
            wait_time = float(self.time_entry.get())
        except ValueError:
            self.instructions_label.config(text="Tempo inválido. Use números.")
            return

        time.sleep(wait_time)
        mouse_position = pyautogui.position()

        self.instructions_label.config(text=f"Posição do mouse: {mouse_position}")

        self.log_text.insert(tk.END, f"{mouse_position}\n")
        self.log_text.see(tk.END)  

        self.log_text.bind("<Button-1>", lambda event: self.log_text.focus_set())
        self.log_text.bind("<Control-a>", lambda event: self.log_text.tag_add(tk.SEL, "1.0", tk.END))
        self.log_text.bind("<Control-c>", lambda event: self.log_text.clipboard_clear())
        self.log_text.bind("<Control-c>", lambda event: self.log_text.clipboard_append(self.log_text.selection_get()), add="+")

if __name__ == "__main__":
    app = MousePositionLogger()
    app.mainloop()