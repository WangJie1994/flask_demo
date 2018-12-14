from flask import Flask
# from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>bad request</h1>', 400


# @app.route('/')
# def index():
#     response = make_response('<h1>this document carries a cookie</h1>')
#     response.set_cookie('answer', '42')
#     return response

@app.route('/')
def index():
    # abort(404)
    return redirect('http://www.example.com')


if __name__ == '__main__':
    app.run(debug=True)
