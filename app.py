import os
import time
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=5432,
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppass"),
    )

def init_db():
    for _ in range(30):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits "
                "(id SERIAL PRIMARY KEY, created_at TIMESTAMP DEFAULT NOW())"
            )
            conn.commit()
            cur.close()
            conn.close()
            return
        except Exception as e:
            print("Menunggu database...", e, flush=True)
            time.sleep(2)

@app.route("/")
def hello():
    return "Halo dari Flask + PostgreSQL + Docker + Jenkins!"

@app.route("/db")
def db_check():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES")
    cur.execute("SELECT COUNT(*) FROM visits")
    total = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(status="terhubung ke database", total_kunjungan=total)

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)