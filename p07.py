import tkinter as tk
from tkinter import messagebox
import random

class KockaDobas:
    def __init__(self, master):
        self.master = master
        self.master.title("Kockadobások statisztikája")
        self.master.geometry("600x500")

        self.dobasok_szama = 10
        self.eredmenyek = [0 for _ in range(7)]

        # Cím
        self.cim = tk.Label(self.master, text="Kattints a gombra!", font=("Ariel", 16))
        self.cim.grid(row=0, column=1, pady=20)

        # Bemeneti mező a dobások számának
        self.dobasok_szama_bemenet = tk.StringVar(value="10")
        self.dobasszam = tk.Entry(self.master, textvariable=self.dobasok_szama_bemenet, width=10)
        self.dobasszam.grid(row=1, column=0, pady=20, padx=50)

        # Dobás gomb
        self.gomb = tk.Button(self.master, text="Dobás", command=self.on_dobas)
        self.gomb.grid(row=1, column=2, pady=20)

        # Eredmény címke
        self.eredmeny_cimke_szovege = tk.StringVar(value="......")
        self.eredmeny_cimke = tk.Label(self.master, textvariable=self.eredmeny_cimke_szovege, font=("Ariel", 16))
        self.eredmeny_cimke.grid(row=2, column=1, pady=20)

        # Kilépés gomb
        self.kilepes = tk.Button(self.master, text="Kilépés", command=self.master.destroy, bg="red")
        self.kilepes.grid(row=1, column=3, pady=20, padx=40)

        # Alapértelmezett dobás
        self.on_dobas()

        # Fő ciklus indítása
        # self.master.mainloop()

    def dobas(self, dobasok):
        """A dobások elvégzése és az eredmény frissítése"""
        #eredmenyek = [0 for _ in range(7)]
        for _ in range(dobasok):
            szam = random.randint(1, 6)
            self.eredmenyek[szam] += 1

        self.eredmeny_cimke_szovege.set(
            f"1 - {self.eredmenyek[1]} \n"
            f"2 - {self.eredmenyek[2]} \n"
            f"3 - {self.eredmenyek[3]} \n"
            f"4 - {self.eredmenyek[4]} \n"
            f"5 - {self.eredmenyek[5]} \n"
            f"6 - {self.eredmenyek[6]}"
        )

    def on_dobas(self):
        """A dobás gomb eseménykezelője"""
        try:
            self.dobasok_szama = int(self.dobasok_szama_bemenet.get())
            self.dobas(self.dobasok_szama)
        except ValueError:
            messagebox.showerror("Hiba", "Rossz értéket adott meg!")


# Program indítása
if __name__ == "__main__":
    root = tk.Tk()
    app = KockaDobas(root)
    root.mainloop()


