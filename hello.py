from flask import Flask
import bugsnag
import bugsnag.flask

app = Flask(__name__)
bugsnag.configure()
bugsnag.flask.handle_exceptions(app)

@app.route("/")
def hello():
    print "hi"
    return "Hello World!"

@app.route('/raise')
def myraise():
    raise Exception('u r bad')

if __name__ == "__main__":
    app.run()