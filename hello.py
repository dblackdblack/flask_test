from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print "hi"
    return "Hello World!"

@app.route('/raise')
def myraise():
    raise Exception('u r bad')

if __name__ == "__main__":
    app.run()