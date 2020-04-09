from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#this

app = Flask(__name__) # NAME OF FILE
app.config['SQLALCHEMY_DATABASE_URI'] = '''postgres://postgres:Kieran@localhost:5432/todoapp'''
db = SQLAlchemy(app)

class Todo(db.Model):
    __tbalename__ = 'todos'
    id= db.Column(db.Integer, primary_key=True)
    description =db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])

