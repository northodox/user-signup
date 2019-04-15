from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('index.html')

@app.route("/welcome", methods = ["POST"])
def welcome():
    username = request.form['username']
    return render_template('welcome-page.html')

app.run()