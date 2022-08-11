from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html/home")

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html/")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)