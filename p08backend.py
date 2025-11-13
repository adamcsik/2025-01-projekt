from flask import Flask, jsonify
import random
import sqlite3


def init_db():
    conn = sqlite3.connect("kocka_API.db")
    db = conn.cursor()
    db.execute(
        "CREATE TABLE IF NOT EXISTS kocka (dobasok INT, egy INT, ket INT, harom INT, negy INT, ot INT, hat INT)")
    conn.commit()
    conn.close()


app = Flask(__name__)
@app.route("/api/data")
def get_data():
    szam = random.randint(10, 500)
    return jsonify({"uzenet": f"{szam}"})

@app.route("/api/osszesites")
def osszesites():
    conn = sqlite3.connect("kocka_API.db")
    db = conn.cursor()
    db.execute("SELECT egy, ket, harom, negy, ot, hat FROM kocka")
    sorok = db.fetchall()
    conn.close()
    osszes = [sum(sor[i] for sor in sorok) for i in range(6)]
    return jsonify({"osszesites" : osszes})

@app.route("/api/dobas/<int:dbszam>")
def dobas(dbszam):
    if dbszam <= 0:
        dbszam = 10
    eredmenyek = [0] * 7
    for _ in range(dbszam):
        szam = random.randint(1, 6)
        eredmenyek[szam] += 1

    conn = sqlite3.connect("kocka_API.db")
    db = conn.cursor()
    db.execute(
        "INSERT INTO kocka (dobasok, egy, ket, harom, negy, ot, hat) VALUES (?, ?, ?, ?, ?, ?, ?)", (
            dbszam, eredmenyek[1], eredmenyek[2], eredmenyek[3], eredmenyek[4],eredmenyek[5],eredmenyek[6]
        ))
    conn.commit()
    conn.close()

    return jsonify({"eredmenyek": eredmenyek[1:]})

if __name__ == "__main__":
    init_db()
    app.run(port=5000)
