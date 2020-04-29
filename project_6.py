# Project 6
# A "Help" button 

from tkinter import *
import tkinter.messagebox

class ToolBar:

    SUBJECT_FONT = ('Helvetica', 10, 'bold')
    FONT = ('Helvetica', 10)
    
    def __init__(self, master):
        self.master = master
        self.main_menu = Menu(self.master)
        self.master.configure(menu = self.main_menu)
        self.sub_menu = Menu(self.main_menu)
        self.sub_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label = "Help", menu = self.sub_menu)
        self.sub_menu.add_command(label = "FAQs",
                                  command = self.help_window)
        self.sub_menu.add_command(label = "Support", command = self.support)       

    
    def help_window(self):
        self.new_window = Toplevel(self.master)
        self.new_window.geometry("300x400")
        self.new_window.title("FAQs")
        self.label_1 = Label(self.new_window, text = "About us",
                       font = self.SUBJECT_FONT)
        self.label_1.pack()
        self.label_2 = Label(self.new_window,
                             text = "A very long text about us or something"
                             + " blah blah blah blah blah blah blah blah blah"
                             + "blah blah blah blah blah blah blah blah blah",
                             font = self.FONT,
                             wraplength = 250, anchor = W,
                             justify= LEFT)
        self.label_2.pack()

               
    def support(self):
        tkinter.messagebox.showinfo("Support", "Call us at 0000000")
           

if __name__ == "__main__":
    window = Tk()
    window.title("Now Is the Time to Panic!")
    window.geometry("400x500")
    toolbar = ToolBar(window)
    window.mainloop()

