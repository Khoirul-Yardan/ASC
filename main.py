# main.py

from gui.app_gui import AutoSecureCapsuleApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoSecureCapsuleApp(root)
    root.mainloop()
