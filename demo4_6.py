from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import session
from flask import url_for
from flask import redirect
from flask import flash


class NameForm(Form):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have change your name!')
        session['name'] = form.name.data
        # name = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index_4_3.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug=True)
