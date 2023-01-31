from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = "8b23979b7b34205befd9774ac624031c"


posts = [
    {
        'author': 'Kev Jam',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 1, 2023'
    }, {
        'author': 'Kri Jam',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 2, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
