from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__) # create new flask application with this file name

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

# Flask is designed in terms of route
@app.route("/", methods=["GET", "POST"])
def index():
    if session.get('notes') is None:
	    session['notes'] = []

    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)
        #notes.append(note)

    return render_template("index.html", notes=session['notes'])

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return 'Please submit the form!!'
	else:
		name = request.form.get('name')
		return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()