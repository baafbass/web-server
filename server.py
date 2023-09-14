from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/experience.html')
def experience():
    return render_template('experience.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('formresult1.html')
    else:
        return 'Something went wrong. Try again'
