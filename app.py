from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("rent_data.db")
    df = pd.read_sql("SELECT * FROM rent_table LIMIT 5000", conn)
    conn.close()
    return df

@app.route("/", methods=["GET"])
def home():
    df = get_data()
selected_location = request.args.get("location")

# get full list first
all_locations = df["Location"].dropna().unique()

# apply filter ONLY if valid
if selected_location and selected_location != "":
    df = df[df["Location"] == selected_location]
    locations = all_locations

    # category count (for chart)
    category_counts = df["rent_category"].value_counts().to_dict()

    return render_template(
        "index.html",
        data=data,
        avg_rent=avg_rent,
        total=total,
        locations=locations,
        selected_location=selected_location,
        category_counts=category_counts
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
