from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("rent_data.db")
    df = pd.read_sql("SELECT * FROM rent_table LIMIT 200", conn)
    conn.close()
    return df

@app.route("/")
def home():
    df = get_data()

    data = df.to_dict(orient="records")
    avg_rent = round(df['VALUE'].mean(), 2)
    total = len(df)

    return render_template("index.html", data=data, avg_rent=avg_rent, total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
