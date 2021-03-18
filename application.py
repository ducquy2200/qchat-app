from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'Doducquy22.'

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
