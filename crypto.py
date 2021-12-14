from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "Welcome to the Machine Learning crypto application."

@app.route("/admin")
def admin():
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()

