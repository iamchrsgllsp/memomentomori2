from flask import (
    Flask,
    render_template,
    send_from_directory,
    url_for,
    request,
    redirect,
    session
)
import os
import requests
import json
import match
import uuid
from invitecodes import codes

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
   return render_template("index.html")

@app.route("/find", methods=["GET", "POST"])
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

@app.route('/match',methods=["GET", "POST"])
def matcher():
    data = match.matcher(1)
    return render_template('found.html', data=data)

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        return f"POST"
    else:
        link = [
            "https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/06/loki-still02.jpg"
        ]
        return render_template("test.html", images=link)
    
@app.route('/invite', methods=['GET', 'POST'])
def inviter():
  if request.method == "POST":
    email = request.form['email']
    print(email)
    geninvite = uuid.uuid4()
    with open("test.txt", "w") as f:
      f.write(str(geninvite))
      codes.append({"userid": 1, "email": email, "invitecode": str(geninvite)})
    return f"Email has been sent to {email}<br>User can click: <a href='http://127.0.0.1:5000/invited/{geninvite}'>here</a> to join the meetin"
  else:
    return render_template("invite.html")


@app.route('/invited/<invitecode>', methods=["GET", "POST"])
def invited(invitecode):
  data = ""
  if request.method == "POST":
    email = request.form['email']
    for i in codes:
      if i['email'] == email:
        data = "success"
    return data
  else:
    return render_template("invitecode.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "images/favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
