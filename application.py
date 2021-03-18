from flask import Flask, render_template
from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'Doducquy22.'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ywbnoztyucofwo:f770a5fb7b4ebc3df8f2b59d682c2f87f409142b36bd8248b36a07c046b03808@ec2-54-164-22-242.compute-1.amazonaws.com:5432/d1mp446fh6pe2b'
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Insert into DB"
    return render_template("index.html", form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)
