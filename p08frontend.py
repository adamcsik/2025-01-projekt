import tkinter as tk
from tkinter import messagebox
import  requests
import p07n

class KockaApp(p07n.KockaDobasMentes):
    def __init__(self, master, auto_roll=False):
        super().__init__(master, auto_roll=auto_roll)

        self.api_gomb = tk.Button(root, text="Lekérés", command=self.adatkeres)
        self.api_gomb.grid(row=4, column=0, pady=10)

        self.api_cimke = tk.Label(root, text="...")
        self.api_cimke.grid(row=4, column=1, pady=10)

        self.api_dobas_gomb = tk.Button(self.master, text="Dobás a Back-ben", command=self.api_dobas)
        self.api_dobas_gomb.grid(row=5, column=0, pady=10)

        self.api_osszes_gomb = tk.Button(self.master, text="Összesítés a Back-ből", command=self.api_osszes)
        self.api_osszes_gomb.grid(row=5, column=2, pady=10)

    def api_osszes(self):
        try:
            valasz = requests.get(f"http://localhost:5000/api/osszesites", timeout=3)
            valasz.raise_for_status()
            adat = valasz.json()
            osszes = adat["osszesites"]
            self.osszes_cimke_szovege.set(
                "\n".join(f"{i + 1} - {osszes[i]}" for i in range(6))
            )
        except:
            messagebox.showerror("Hiba", "Nem sikerült az összesítés kapcsolatot létrehozni!")

    def api_dobas(self):
        try:
            dbszam = int(self.dobasok_szama_bemenet.get())
            valasz = requests.get(f"http://localhost:5000/api/dobas/{dbszam}", timeout=3)
            valasz.raise_for_status()
            adat = valasz.json()
            eredmenyek = adat["eredmenyek"]
            self.eredmeny_cimke_szovege.set("\n".join(f"{i+1} - {eredmenyek[i]}" for i in range(6)))
        except:
            messagebox.showerror("Hiba", "Nem sikerült a dobás kapcsolatot létrehozni!")

    def adatkeres(self):
        try:
            valasz = requests.get("http://localhost:5000/api/data", timeout=3)
            valasz.raise_for_status()
            adat = valasz.json()
            self.api_cimke.config(text=adat["uzenet"])
            app.dobasok_szama_bemenet.set(adat["uzenet"])
        except:
            messagebox.showerror("Hiba", "Nem sikerült a kapcsolat!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root, auto_roll=True)
    root.mainloop()
