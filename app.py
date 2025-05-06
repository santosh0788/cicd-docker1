from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome'
@app.route('/user')
def user():
    return 'sai teja'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
