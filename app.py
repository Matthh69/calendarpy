from flask import Flask, render_template
# add commit pull push
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')  # "<p>Hello, World!</p>"
