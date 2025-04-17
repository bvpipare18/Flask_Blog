from flask import Flask, render_template
app = Flask(__name__)


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
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)