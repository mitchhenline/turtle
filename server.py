from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4590, host = "localhost")