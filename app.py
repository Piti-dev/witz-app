import os
from flask import Flask, jsonify
import random
import sqlite3

app = Flask(__name__)

witze = [
    "Chuck Norris kann Drehtüren zuschlagen",
    "Chuck Norris hat bis unendlich gezählt, zweimal",
    "Chuck Norris kann Zwiebeln zum weinen bringen"
]

def get_db_connection():
    conn = sqlite3.connect("witze.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/witz")
def zufallswitz():
    conn = get_db_connection()
    witz = conn.execute("SELECT inhalt FROM witze ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.close()
    return jsonify({"witz": witz["inhalt"]})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))