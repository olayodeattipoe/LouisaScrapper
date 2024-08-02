from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all domains
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:bolatito224@localhost:3306/learnhub"

db.init_app(app)


@app.route('/')
def hello_world():
    from database import fetch_tables
    return list(fetch_tables())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
