from flask import (
    Flask,
    render_template,
    send_from_directory,
    url_for,
    request,
    redirect,
)
import os
import requests
import json

app = Flask(__name__, static_folder="static")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        postcode = request.form["postcode"]
        return redirect(f"/found/{postcode}")
    else:
        return render_template("home.html")


@app.route("/found/<postcode>")
def found(postcode):
    justeat = "https://uk.api.just-eat.io/restaurants/bypostcode/" + postcode
    data = requests.get(
        justeat,
        headers={
            "Content-Type": "text/html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        },
    )
    data = json.loads(data.content)
    data = data["Restaurants"]
    return render_template("restaurants.html", restaurants=data)


@app.route("/about")
def about():
    return "about"


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        return f"POST"
    else:
        link = [
            "https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/06/loki-still02.jpg"
        ]
        return render_template("test.html", images=link)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "images/favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
