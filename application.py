from flask import Flask, render_template, redirect, url_for
from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'secret'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ywbnoztyucofwo:f770a5fb7b4ebc3df8f2b59d682c2f87f409142b36bd8248b36a07c046b03808@ec2-54-164-22-242.compute-1.amazonaws.com:5432/d1mp446fh6pe2b'
db = SQLAlchemy(app)

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

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation successful
    if login_form.validate_on_submit():
        return 'Logged in, finally!'

    return render_template("login.html", form=login_form)



if __name__ == "__main__":
    app.run(debug=True)
