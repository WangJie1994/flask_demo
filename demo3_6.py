from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template
from datetime import datetime


app = Flask(__name__)
booststrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('user_bs.html', current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
