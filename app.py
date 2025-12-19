from os import environ
from flask import Flask, render_template

flask_port = environ.get("Flask_port")

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("base.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=flask_port, debug=True)
