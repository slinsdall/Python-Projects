from tkinter import *
import tkinter as tk
from tkinter import messagebox


import studenttracking_func
import studenttracking_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,300)
        studenttracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="lightblue")
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracking_func.ask_quit(self))
        arg = self.master


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
