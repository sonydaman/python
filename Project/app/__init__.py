from flask import Flask, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask('app')
app.config.update(
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///../database.db'        
    )
db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'Blog be here'


# project/run.py
from app import app

if __name__ == '__main__':
    app.run(debug=True)