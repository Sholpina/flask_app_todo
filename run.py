
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = "some secret key"

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/loginuser')
def loginuser():
    return render_template("loginuser.html")


@app.route('/signupuser')
def signupuser():
    return render_template("signupuser.html")


@app.route('/currenttodos')
def currenttodos():
    return render_template("currenttodos.html")


@app.route('/createtodo')
def createtodos():
    return render_template("createtodos.html")


@app.route('/completedtodos')
def completedtodos():
    return render_template("completedtodos.html")


@app.route('/viewtodo')
def viewtodo():
    return render_template("viewtodo.html")


if __name__ == "__main__":
    app.run(debug=True)

db.create_all()
