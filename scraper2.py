from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

def scraper():
    result = []
    df = pd.read_csv('data.csv')
    column_names = df.columns

    for col in column_names:
        obj = {}
        obj[col] = df[col].tolist()
        result.append(obj)
    return result


@app.route("/data")
def data():
    scraper_data = scraper()
    return jsonify(scraper_data)




if __name__ == "__main__":
    app.run(debug=True)
