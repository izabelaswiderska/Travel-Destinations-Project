import tkinter as tk
import application.gui.app as application

"""
    main function creates the root for the app GUI    
"""


def main():
    root = tk.Tk()
    app = application.App(root)
    root.mainloop()

