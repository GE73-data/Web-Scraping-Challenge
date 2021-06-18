from flask import Flask, render_template, redirect
from datetime import datetime
import scrape_mars
import pymongo
import json

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

app = Flask(__name__)


@app.route("/scrape")
def scrape_data():
    scraped_data = scrape_mars.scrape()
    mars_db = client.mars_db
    data = mars_db.summary_data
    data.delete_many({})
    data.insert(scraped_data)
    return redirect("/", code=302)

@app.route("/")
def index():
    mars_db = client.mars_db
    data = mars_db.summary_data.find_one()
    # print(data)
    return render_template("index.html", data=data, current_time=datetime.utcnow())


if __name__ == "__main__":
    app.run(debug=True)