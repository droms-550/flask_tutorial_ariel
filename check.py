from flask import Flask

app = Flask(__name__)


"Default page"
"""@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"""


from markupsafe import escape

"Variable name"
"""@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"""


from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))