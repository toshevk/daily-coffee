from flask import Flask, render_template
import request

app = Flask(__name__)

quote_of_the_day = request.retrieve_quote()
photo_of_the_day = request.retrieve_photo()

@app.route("/")
def home():
    return render_template("index.html", image="static/images/img.jpg", quote=quote_of_the_day)

if __name__ == "__main__":
    app.run()
