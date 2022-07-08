import tkinter as tk
from tkinter import BOTTOM, TOP, ttk
from datetime_utils_moj import *
from tkinter.colorchooser import askcolor



root = tk.Tk()
root.title('Smart Home')
root.configure(bg="#282828")
root.geometry("500x600")
frame0 = tk.Frame(root, width=400, height=280, bg="#3ADF00")


def create_datetime_frame():
    def refresh_time():
        now_time = formatted_time()
        time_label.configure(text=now_time)
        time_label.after(1000, refresh_time)

    datetime_frame = tk.Frame(
        root, width=100, height=50, bg="#282828"
    )
    datetime_frame.pack(side=TOP)

    today = formatted_date()
    now_time = formatted_time()

    date_label = tk.Label(
        datetime_frame, bg="#282828", fg="white",
        text=today, font=("Arial", 15)
    )
    date_label.pack(side=TOP)
    time_label = tk.Label(
        datetime_frame, bg="#282828", fg="white",
        text=now_time, font=("Arial", 20)
    )
    time_label.pack(side=TOP)
    refresh_time()



def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])





notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)


frame1 = tk.Frame(notebook, width=400, height=280, bg="#3ADF00")
frame2 = tk.Frame(notebook, width=400, height=280, bg="#B40431")
frame3 = tk.Frame(notebook, width=400, height=280, bg="#2E64FE")
frame4 = tk.Frame(notebook, width=400, height=280, bg="#FFFF00")
frame5 = tk.Frame(notebook, width=400, height=280, bg="#848484")
frame6 = tk.Checkbutton(frame5, text= "Vrijeme", command=create_datetime_frame, onvalue=1, offvalue=0)
frame7 = tk.Checkbutton(frame5, text='Odaberite boju', command=change_color).pack(expand=True)
frame8 = tk.Frame(notebook, width=400, height=280, bg="#2EFEF7")




frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)
frame8.pack(fill='both', expand=True)

notebook.add(frame1, text='TV')
notebook.add(frame2, text='Grijanje')
notebook.add(frame3, text='Rasvjeta')
notebook.add(frame4, text='Ulazna vrata')
notebook.add(frame5, text='Settings')
notebook.add(frame8, text='Meteo')




root.mainloop()

