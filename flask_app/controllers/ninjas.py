# controllers.ninjas

from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def display_page():
    """Show create ninja page"""
    dojos = Dojo.show_all_dojos()
    return render_template('ninjas.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def add_ninja():
    """Add a new ninja to a particular dojo"""
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    path = f"/dojos/{request.form['dojo_id']}"
    return redirect(path)
