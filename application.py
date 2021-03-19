import os
from flask import Flask, render_template, redirect, url_for, flash
from wtform_fields import *
from models import *
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from time import localtime, strftime

# Configure app
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ywbnoztyucofwo:f770a5fb7b4ebc3df8f2b59d682c2f87f409142b36bd8248b36a07c046b03808@ec2-54-164-22-242.compute-1.amazonaws.com:5432/d1mp446fh6pe2b'
db = SQLAlchemy(app)
# Initialize Flask-SocketIO
socketio = SocketIO(app)
ROOMS = ["lounge", "news", "games", "coding"]

# Configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Updated database if validation successful
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_pswd = pbkdf2_sha256.hash(password)

        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        flash('Register successfully. Please login.', 'success')

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation successful
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
def chat():

    # if not current_user.is_authenticated:
    #     flash('Please login.', 'danger')
    #     return redirect(url_for('login'))

    return render_template('chat.html', username=current_user.username, rooms=ROOMS)

@app.route("/logout", methods=['GET'])
def logout():

    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))

@socketio.on('message')
def message(data):

    print(f"\n\n{data}\n\n")
    send({'msg': data['msg'], 'username': data['username'], 'time_stamp': strftime('%b-%d %I: %M%p', localtime())}, room=data['room'])

@socketio.on('join')
def join(data):

    join_room(data['room'])
    send({'msg': data['username'] + " has joined the " + data['room'] + " room."}, room=data['room'])

@socketio.on('leave')
def leave(data):

    leave_room(data['room'])
    send({'msg': data['username'] + " has left the " + data['room'] + " room."}, room=data['room'])

if __name__ == "__main__":
    app.run()
