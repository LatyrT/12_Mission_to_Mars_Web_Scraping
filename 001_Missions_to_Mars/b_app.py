from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import pymongo
import a_scrape_Mars

# Create an instance of our Flask app.
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/MarsScraping_app"
mongo = PyMongo(app)

#----------------------------
# Data Scraping
#----------------------------

@app.route("/scrape")
def scraper():
    # Calls the scrape func from the required file
    Mars_Scraping = a_scrape_Mars.scrape()

    # Drops collection if available to remove duplicates
    mongo.db.MarsData_Coll.drop()
    
    # Create new collection
    MarsData_Coll = mongo.db.MarsData_Coll

    # Insert data into mongo
    #MarsData_Coll.insert_many(Mars_Scraping) ----- did not work
    MarsData_Coll.update({}, Mars_Scraping, upsert=True)
    return redirect("/", code=302)

#----------------------------
# Home page
#----------------------------

@app.route('/')
def index():
    # find data
    Mars_Data = mongo.db.MarsData_Coll.find_one()
    print(Mars_Data)

    # Return the template with the Mars_Data list passed in
    return render_template('index.html', Mars_Data=Mars_Data)

if __name__ == "__main__":
    app.run(debug=True)







































