from flask import Flask, render_template, url_for, redirect, request
import requests
import os
import forms
import database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'spongebob'


# IGNORE THIS, THIS ALLOWS US TO OVERRIDE 
# ENV VARIABLES IF SOMEONE IS NOT USING DOCKER
#
# if 'DB_URL' in os.environ:
#    app.config['DB_URL'] = os.getenv('DB_URL')
#else:
#    app.config['DB_URL'] = 'http://localhost:3000/api'
#print("DB URL: " + app.config['DB_URL'])
# 
# END OF THAT MESS ABOVE


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/people')
def showPeople():
    return render_template("people.html", people=database.GetThePeople())

@app.route('/insert', methods=['GET' , 'POST'])
def insert():
    form = forms.InsertForm()
    if request.method == "POST":
        response = database.AddPerson(form.fname.data, form.lname.data)
        if response.status_code == 201:
            return(redirect(url_for('showPeople')))
        else:
            return(redirect(url_for('insert')))
    return render_template("insert.html", form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)