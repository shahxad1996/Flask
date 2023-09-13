from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/form",methods=['get','post'])
def form():
    if request.method ==' GET':
        return render_template('form.html')
    else:
        math = float(request.form['math'])
        computer = float(request.form['computer'])
        english = float(request.form['english'])
        average = (math+computer+english)/3
        
        return render_template("index.html",score = average)




if __name__ == "__main__":
    app.run(debug=True)