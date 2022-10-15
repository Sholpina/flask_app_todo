from unicodedata import name
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
    return "Hello there, Are you excited"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    db.create_all()

