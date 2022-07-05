# controllers.dojos
from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    """For this assignment redirect to dojos page"""
    return redirect('/dojos')

@app.route('/dojos')
def show_all():
    """Render All the dojos"""
    dojos = Dojo.show_all_dojos()
    print(dojos)
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def add_dojo():
    """Add a dojo location to the list"""
    # Create data dict based on request form
    # The keys must match to exactly the variables in query string
    data = {
        'name': request.form['name']
    }
    # Pass the data dict to create_dojo() in Dojo class
    Dojo.create_dojo(data)
    # Redirect back to dojos page
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_all_ninja(dojo_id):
    """Show all the ninja of a particular dojo"""
    data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_dojo_and_all_ninjas(data)
    return render_template('dojo_show.html', all_ninjas=ninjas)
