from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    df = pd.read_csv("count_result (3).csv")

    result = {}

    for index, row in df.iterrows():

        name = row["object"]
        count = int(row["count"])

        result[name] = {
            "current": count
        }

    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)