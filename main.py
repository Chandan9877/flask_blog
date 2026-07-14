from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author' : 'Corey Schafer',
        'title' : "Blog post 1",
        'content' : 'First post content',
        'date_posted' : 'jul 10 , 2026'
    },
    {
        'author' : 'Jane Doe',
        'title' : "Blog post 2",
        'content' : 'Second post content',
        'date_posted' : 'jul 11 , 2026'
    },
    {
        'author' : 'Marry Joe',
        'title' : "Blog post 3",
        'content' : 'Third post content',
        'date_posted' : 'jul 12 , 2026'
    }
]

@app.route("/")
def home():
    return render_template("home.html",posts = posts,title = 'Home')

@app.route("/about")
def about():
    return render_template("about.html",title = 'About')

if __name__ == "__main__":
    app.run(debug=True)