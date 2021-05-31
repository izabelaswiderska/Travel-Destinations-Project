from tkinter import messagebox as msb

"""
    additional methods that are used to display messagebox with information about possible errors that might've occurred  
"""


def empty_input_messagebox():
    msb.showinfo('Incorrect country name', 'First enter country name')


def input_error_messagebox():
    msb.showerror('Incorrect country name', 'Entered country doesn\'t exist')


def incorrect_text_format_messagebox():
    msb.showerror('Incorrect text format', 'Unable to save all the info because of incorrect text format')



