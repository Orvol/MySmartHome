import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Smart Home')
root.configure(bg="#282828")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = tk.Frame(notebook, width=400, height=280, bg="#3ADF00")
frame2 = tk.Frame(notebook, width=400, height=280, bg="#B40431")
frame3 = tk.Frame(notebook, width=400, height=280, bg="#2E64FE")
frame4 = tk.Frame(notebook, width=400, height=280, bg="#FFFF00")
frame5 = tk.Frame(notebook, width=400, height=280, bg="#848484")

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)

notebook.add(frame1, text='TV')
notebook.add(frame2, text='Grijanje')
notebook.add(frame3, text='Rasvjeta')
notebook.add(frame4, text='Ulazna vrata')
notebook.add(frame5, text='Settings')

root.mainloop()
