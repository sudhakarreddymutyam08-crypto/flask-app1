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


    all_locations = df["Location"].dropna().unique()

    selected_location = request.args.get("location")


    if selected_location and selected_location != "":
        df = df[df["Location"] == selected_location]

    locations = all_locations


    data = df.to_dict(orient="records")
    total = len(df)


    if len(df) > 0:
       avg_rent = round(df['VALUE'].mean(), 2)
    else:
       avg_rent = 0


    if "rent_category" in df.columns:
         category_counts = df["rent_category"].value_counts().to_dict()
    else:
         category_counts = {}

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
