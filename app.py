from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():  # put application's code here
    return render_template("base.html")


if __name__ == '__main__':
    host = environ.get("FLASK_RUN_HOST")
    flask_port = int(environ.get("FLASK_RUN_PORT"))
    app.run(host=host, port=flask_port, debug=True)
