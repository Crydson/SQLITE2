
import tkinter as tk

import sqlite3 as sql

try:
    conn = sql.connect("Segundo_Database.db")
except:
    print("Falha ao conectar")

window = tk.Tk()

window.title("Segundo_DB_Program")

label = tk.Label(window, text = "hello world ", background= "grey", foreground= "white", width= 100, height= 100).pack()

tk.mainloop()