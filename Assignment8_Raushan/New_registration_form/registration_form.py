from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)

# Secret key
app.config['SECRET_KEY'] = 'mysecretkey'

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)   # UNIQUE
    email = db.Column(db.String(100), unique=True)     # UNIQUE


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        # 🔥 Check if user already exists
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            return "User already exists!"

        # Save new user
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            username=form.username.data,
            email=form.email.data
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('success'))

    return render_template('register.html', form=form)


@app.route('/success')
def success():
    users = User.query.all()
    return render_template('confirm.html', users=users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)