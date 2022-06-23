from flask import Flask, render_template, jsonify, redirect
import pymongo
from scrape import scrape


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars

app = Flask(__name__)


@app.route("/")
def index():
    db_list = client.list_database_names()
    if "mars" in db_list:
        mars = list(db.collection.find())[0]
        return  render_template('index.html', mars=mars)



@app.route("/scrape")
def test():
    db.collection.delete_many({})
    mars_new_scrap = scrape()
    db.collection.insert_one(mars_new_scrap)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)