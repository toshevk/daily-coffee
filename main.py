from flask import Flask, render_template, request
from request import retrieve_quote, retrieve_photo

app = Flask(__name__)

quote_of_the_day = retrieve_quote()
retrieve_photo()

@app.route("/")
def home():
    return render_template("index.html", image="static\img.jpg", quote=quote_of_the_day)

if __name__ == "__main__":
    app.run()
