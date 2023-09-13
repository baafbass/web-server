from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Farid is becoming a great programmer!'