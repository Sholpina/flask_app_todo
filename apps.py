
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




SECRET_KEY = "some secret key"

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return '<h1>Hello everybody!</h1>'
    
@app.route('/loginuser')
def loginuser():
    return '<h1>loginuser!</h1>'

@app.route('/signupuser')
def signupuser():
    return '<h1>signupuser!</h1>'

@app.route('/currenttodos')
def currenttodos():
    return '<h1>currenttodos!</h1>'

@app.route('/createtodo')
def createtodos():
    return '<h1>createtodo!</h1>'

@app.route('/completedtodos')
def completedtodos():
    return '<h1>completedtodos!</h1>'

@app.route('/viewtodo')
def viewtodo():
    return '<h1>vviewtodo!</h1>'


if __name__ == "__main__":
    app.run(debug=True)

db.create_all()

