import tkinter as tk 
from tkinter import ttk
from tkcalendar import Calendar

def show_calendar():
    window = tk.Toplevel()
    window.title('Calendário')

    cal = Calendar(window, selectmode='day', year=2024, month=3, day=22)
    cal.pack(pady=20)



root = tk.Tk()
root.title('Exibir calendário')
root.geometry('300x200')

btn = (ttk.Button(root, text='Calendário', command=show_calendar).pack(pady=10))
root.mainloop()