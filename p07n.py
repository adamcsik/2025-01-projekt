import csv
import sqlite3
import tkinter as tk
from tkinter import messagebox
import p07

class KockaDobasMentes(p07.KockaDobas):
    def __init__(self, master, auto_roll=False):
        super().__init__(master, auto_roll=auto_roll)

        """self.mentes_txt = tk.Button(self.master, text="Mentés txt fájlba", command=self.mentes_txtbe)
        self.mentes_txt.grid(row=3, column=0, pady=10)

        self.mentes_csv = tk.Button(self.master, text="Mentés csv fájléba", command=self.mentes_csvbe)
        self.mentes_csv.grid(row=3, column=1)

        self.mentes_sql = tk.Button(self.master, text="Mentés SQL-be", command=self.mentes_sql)
        self.mentes_sql.grid(row=3, column=2)
        """
        # Összesítés címke
        self.osszes_cimke_szovege = tk.StringVar(value="......")
        self.osszes_cimke = tk.Label(self.master, textvariable=self.osszes_cimke_szovege, font=("Ariel", 16))
        self.osszes_cimke.grid(row=2, column=2, pady=20)

    def mentes_sql(self):
        try:
            conn = sqlite3.connect("kockadobas.db")
            db = conn.cursor()
            db.execute(
                "CREATE TABLE IF NOT EXISTS kocka (dobasok INT, egy INT, ket INT, ha INT, negy INT,  ot INT, hat INT)")
            db.execute("INSERT INTO kocka VALUES (?, ?, ?, ?, ?, ?, ?)", (self.dobasok_szama,
                                                                          self.eredmenyek[1],
                                                                          self.eredmenyek[2],
                                                                          self.eredmenyek[3],
                                                                          self.eredmenyek[4],
                                                                          self.eredmenyek[5],
                                                                          self.eredmenyek[6])
                       )
            conn.commit()
            conn.close()
            self.osszesites_sql()
        except:
            messagebox.showerror("Hiba", "Nem sikerült az SQL-be mentés!")

    def osszesites_sql(self):
        try:
            conn = sqlite3.connect("kockadobas.db")
            db = conn.cursor()
            db.execute("SELECT egy, ket, ha, negy, ot, hat FROM kocka")
            sorok = db.fetchall()
            osszesen = [0 for _ in range(7)]
            for sor in sorok:
                osszesen[1] += sor[0]
                osszesen[2] += sor[1]
                osszesen[3] += sor[2]
                osszesen[4] += sor[3]
                osszesen[5] += sor[4]
                osszesen[6] += sor[5]
            conn.close()

            self.osszes_cimke_szovege.set(
                f"1 - {osszesen[1]} \n"
                f"2 - {osszesen[2]} \n"
                f"3 - {osszesen[3]} \n"
                f"4 - {osszesen[4]} \n"
                f"5 - {osszesen[5]} \n"
                f"6 - {osszesen[6]}"
            )
        except:
            messagebox.showerror("Hiba", "Nem sikerült az SQL-be mentés!")

    def mentes_csvbe(self):
        fajlnev = "mentes.csv"
        try:
            with open(fajlnev, mode="a", newline="", encoding="utf-8") as csvfajl:
                writer = csv.writer(csvfajl)
                writer.writerow([self.dobasok_szama] + [self.eredmenyek[i] for i in range(1, 7)])
                messagebox.showinfo("Mentés", "Sikeresen mentettem!")
        except:
            messagebox.showerror("Hiba", "Nem sikerült a mentés!")

    def mentes_txtbe(self):
        sor= (f"{self.dobasok_szama}, "
              f"{self.eredmenyek[1]}, {self.eredmenyek[2]}, {self.eredmenyek[3]}, "
              f"{self.eredmenyek[4]}, {self.eredmenyek[5]}, {self.eredmenyek[6]}\n")
        try:
            with open("mentes.txt", "a", encoding="utf-8") as fajl:
                fajl.write(sor)
            messagebox.showinfo("Mentés","Sikeresen mentettem!")
        except:
            messagebox.showerror("Hiba", "Nem sikerült a mentés!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaDobasMentes(root, auto_roll=True)
    root.mainloop()