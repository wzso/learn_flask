from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

## Python’s with statement provides a very convenient way of dealing with
## the situation where you have to do a setup and teardown to make something
## happen. A very good example for this is the situation where you want to gain
## a handler to a file, read data from the file and the close the file handler.
with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')
