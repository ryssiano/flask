from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static/")

@app.route('/')
@app.route('/index')
def index():
     return render_template("index.html")


@app.route('/about')
def about():
     return render_template("about.html")


@app.route('/shop')
def contact():
     return render_template("shop.html")


if __name__ == "__main__":
    app.run(debug=True)
