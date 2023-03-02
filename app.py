from flask import Flask, render_template
# add commit pull push
app = Flask(__name__)


@app.route("/")
def index():
    return render_template ('index.html') #"<p>Hello, World!</p>"
