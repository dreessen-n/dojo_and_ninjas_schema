# controllers.Ninjas

from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models.ninja import Ninja

@app.route('/ninja')
def display_page():
    """Show create ninja page"""
    return render_template('ninjas.html')

@app.route('/ninja/create', methods=['POST'])
def add_ninja():
    """Add a new ninja to a particular dojo"""
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Dojo.create_ninja(data)
    return redirect(f"dojos/{request.form['dojo_id']}")


