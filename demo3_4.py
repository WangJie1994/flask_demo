from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)
booststrap = Bootstrap(app)


@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('index', para=2))
    print(url_for('index', _external=True))
    return render_template('user_bs.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
