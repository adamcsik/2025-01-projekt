import tkinter as tk
from tkinter import messagebox
import  requests
import p07n

def adatkeres():
    try:
        valasz = requests.get("http://localhost:5000/api/data", timeout=3)
        valasz.raise_for_status()
        adat = valasz.json()
        cimke.config(text=adat["uzenet"])
        app.dobasok_szama_bemenet.set(adat["uzenet"])
    except:
        messagebox.showerror("Hiba", "Nem sikerült a kapcsolat!")


root = tk.Tk()
app = p07n.KockaDobasMentes(root)

api_gomb = tk.Button(root, text="Lekérés", command=adatkeres)
api_gomb.grid(row=4, column=0, pady=10)

cimke = tk.Label(root, text="...")
cimke.grid(row=4, column=1, pady=10)

root.mainloop()