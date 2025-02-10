from flask import Flask, render_template
import request

app = Flask(__name__)


@app.route("/")
def home():
    try:
        quote_of_the_day = request.retrieve_quote()
        photo_of_the_day = request.retrieve_photo()
    except Exception as e:
        quote_of_the_day = "I love coffee"
        photo_of_the_day = "static/images/img.jpg"
    return render_template("index.html", image=photo_of_the_day, quote=quote_of_the_day)

if __name__ == "__main__":
    app.run()
