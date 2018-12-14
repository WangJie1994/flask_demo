from flask import request
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, mydict={'key': 2})


if __name__ == '__main__':
    app.run(debug=True)
