"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def usersRedirect():
    return redirect("/users")

@app.route("/users")
def show_users():

    # QUERY DATABASE FOR USERS

    return render_template("user-listing.html")

@app.route("/users/new", methods = ["GET"])
def users_new_form():
    return render_template("add-user.html")

@app.route("/users/new", methods = ["POST"])
def show_new_user_form():
    new_user = User(
        first_name=request.form['first'],
        last_name=request.form['last'],
        image_url=request.form['url']
    )
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    this_user=db.session.get(user_id)
    return render_template("user-details.html", first = this_user.first_name, last = this_user.last_name, url = this_user.image_url)

@app.route("/users/<int:user_id>/edit", method="GET")
def edit_user(user_id):
    this_user=db.session.get(user_id)
    return render_template("edit-user.html", first = this_user.first_name, last = this_user.last_name, url = this_user.image_url)

@app.route("/users/<int:user_id>/edit", method="POST")
def update_user(user_id):

    this_user = db.session.get(user_id)

    this_user.first_name = request.form['first']
    this_user.last_name=request.form['last']
    this_user.image_url=request.form['url']
    
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    db.session.delete(user_id)
    db.session.commit()

    return redirect("/users")




