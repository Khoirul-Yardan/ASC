# GUI Tkinter dasar
# gui/app_gui.py

import tkinter as tk
from tkinter import messagebox
import threading
from core.network_monitor import monitor_network

class AutoSecureCapsuleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoSecure Capsule")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Status: Menunggu untuk memulai monitoring...", wraplength=350)
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Mulai Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Keluar", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_monitoring(self):
        self.label.config(text="Monitoring aktif... pantau log dan alert")
        self.start_button.config(state=tk.DISABLED)
        threading.Thread(target=self.run_monitoring, daemon=True).start()
        messagebox.showinfo("Informasi", "Monitoring jaringan telah dimulai.")

    def run_monitoring(self):
        monitor_network()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoSecureCapsuleApp(root)
    root.mainloop()
