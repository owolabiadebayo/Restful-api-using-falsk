from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)

def get_data():
    url = "http://canews.herokuapp.com/punch"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    img_srcs = [item.get("src").replace("\u0301", "").strip() for item in soup.findAll("img")]
    links = [item.get("href").replace("\u0301", "").strip() for item in soup.findAll("a")]

    data1 = {"imgs": pd.Series(img_srcs), "links": pd.Series(links)}
    data2 = {"imgs": img_srcs, "links": links}
    df = pd.DataFrame(data1)
    df.to_csv("data.csv", index=False)
    return data2

@app.route("/")
def home():
    data = get_data()
    print(data)
    return jsonify(data)



# r=requests.get(url)
# # print(r.content)
# soup = BeautifulSoup(r.content, "html.parser")

# atags = soup.findAll("a")
# hrefs = [item.get("href") for item in atags]

# # print(hrefs)

# text = [item.text.strip() for item in atags]

# # print(text)

# ptagss= soup.findAll("p")
# ptags= soup.findAll("title")

# # print(ptags)
# text = [item.text.strip() for item in ptags ]

# # print(text)

# images = soup.findAll("img")

# # print(images)

# src = [item.get("src") for item in images]

# print(src)







# href=[]
# for item in atags:
#     href.append(item.get("href"))

if __name__ == "__main__":
    app.run(debug=True)