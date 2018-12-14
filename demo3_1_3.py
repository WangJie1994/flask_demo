from flask import request
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('structure_control.html', haha=name, comments=['a', 'b', 'c'])

@app.route('/derivative_page')
def derivative_page():
    return render_template('derivative_page.html')

if __name__ == '__main__':
    app.run(debug=True)
