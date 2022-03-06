from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/products")
def products():
    return render_template('Products.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')
