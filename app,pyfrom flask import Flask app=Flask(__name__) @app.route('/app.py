from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "Hello world"
app.run('0.0.0.0',5000)
