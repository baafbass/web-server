from flask import Flask,render_template,url_for
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    print(url_for('static', filename='computer.png'))
    return render_template('index.html')

@app.route('/about.html')
def aboutme():
    return render_template('about.html')


@app.route('/favicon.ico')
def blog():
    return 'this are my thought on blogs!'

@app.route('/blog/2023/myFam')
def blog2():
    return 'I really love my Familly!'