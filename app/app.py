from flask import Flask, render_template

app = Flask(__name__)

#Routing index
@app.route("/")
def hello_world():
    return render_template('index.html')

#Routing calendar
@app.route('/calendar')
def hello():
    return render_template('calendar.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404