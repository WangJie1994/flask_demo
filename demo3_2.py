from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)
booststrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('user_bs.html')


if __name__ == '__main__':
    app.run(debug=True)