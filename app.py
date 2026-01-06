from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():  # put application's code here
    return render_template("fatbike.html", name="main_page", title="Главная")

@app.route('/fatbike')
def fatbike_page():  # put application's code here
    return render_template("fatbike.html", name="fatbike_page", title="Fat-bike")


if __name__ == '__main__':
    host = environ.get("FLASK_RUN_HOST")
    flask_port = int(environ.get("FLASK_RUN_PORT"))
    app.run(host=host, port=flask_port, debug=True)
