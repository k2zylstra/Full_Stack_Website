from flask import Flask, render_template

app = Flask(__name__) # NAME OF FILE

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])

