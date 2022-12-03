from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/donatello")
def donatello():
    return render_template("donatello.html")

@app.route("/leonardo")
def leonardo():
    return render_template("leonardo.html")

@app.route("/michelangelo")
def michelangelo():
    return render_template("michelangelo.html")

@app.route("/raphael")
def raphael():
    return render_template("raphael.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4590, host = "localhost")