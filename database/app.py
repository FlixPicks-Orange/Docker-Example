from flask import render_template, request, jsonify

import config
from models import Person

import sqlite3
import pandas as pd

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

@app.route("/import_csv")
def import_csv():
    #Connect to SQLite DB
    conn = sqlite3.connect()
    
    # Reads csv file into pandas dataframe
    df = pd.read_csv('data/movies_prestage.db')
    
    # Write the dataframe to a SQLite table
    df.to.sql('movies', conn, index=False, if_exists='replace')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    return "CSV data imported into the 'movies_prestage' database"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
