from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "vicky genius"
def stu():
    return app
app.run('0.0.0.0',5000)
