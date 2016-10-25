from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/helle/<name>')
def hello(name=None):
    return render_template('hell.html',name=name)
