import os
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_session import Session


# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# app = Flask(__name__) # create new flask application with this file name
# app.config["DEBUG"] = 1
# app.config["FLASK_APP"] = development
# app.config["FLASK_CONFIG"] = app.py
# export FLASK_CONFIG=development
# export FLASK_APP=app.py


from app import app

@app.route('/')
def index():
    if not session.get('logged_in'):
        return login()
    else:
        return dashboard()

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if password == 'password' and email == 'admin@gmail.com':
            session['logged_in'] = True
        else:
            flash('wrong password!')
        return index()
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


# Flask is designed in terms of route
# @app.route("/", methods=["GET", "POST"])
# def index():
#     flights = db.execute('SELECT * FROM flights').fetchall()
#     return render_template("index.html", flights=flights)

# @app.route('/book', methods=['POST'])
# def book(name):
#     """ Book a flight"""
#     name = request.form.get('name')
#     try:
#         flight_id = int(request.form.get('flight_id'))
#     except ValueError:
#         return render_template("error.html", message='Invalid flight number.') 
    
#     # Make sure the flight exists.
#     if db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).rowcount == 0:
#         return render_template("error.html", message='No such flight id.')
#     db.execute('INSERT into passangers (name, flight_id) VALUES (:name, :flight_id', {'id': flight_id, 'name': name})
#     db.commit()
#     return render_template('success.html', message='Flight createed successfully')

# @app.route('/flights', methods=['GET', 'POST'])
# def flights():
#     return render_template('hello.html')

# @app.route('/flights/<int:flight_id>', methods=['GET', 'POST'])
# def flight(flight_id):
#     return render_template('hello.html')
