from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def index():
    return "Hello Flask"



@app.route("/about<name>")
def about(name):
    return f"Welcome Mr. {name} to about page."


@app.route("/contact")
def contact():
    return render_template('contact.html')






if __name__ == "__main__":
    app.run(debug=True,)