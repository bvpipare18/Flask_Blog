from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']= '<secret_key>'

# Let us assume we have received this from making a call to DB.
posts = [
    {
        'author': 'Virat Kohli',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '18-Apr-2025'
    },
    {
        'author': 'MS Dhoni',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '19-Apr-2025'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    # If validation is successful then we should alert the messages and redirect to home page.
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # This code executes when we click on submit
    if form.validate_on_submit():
        if form.email.data == 'sample@sample.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)