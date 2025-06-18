from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world from santosh'
@app.route('/one')
def one():
    return render_template('one.html')
@app.route('/two')
def two():
    return render_template('two.html')
@app.route('/three')
def three():
    return render_template('three.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#hi