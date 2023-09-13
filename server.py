from flask import Flask,render_template,url_for
app = Flask(__name__)

print(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None,post_id=None):
    return render_template('index.html', name = username,post_id = post_id)

@app.route('/about.html')
def aboutme():
    return render_template('about.html')


@app.route('/favicon.ico')
def blog():
    return 'this are my thought on blogs!'

@app.route('/blog/2023/myFam')
def blog2():
    return 'I really love my Familly!'