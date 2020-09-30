from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>Lab OpenShift</h1><p>Hola, Tepic!</p>", 200, { 'Content-Type': 'text/html' }

if __name__ == '__main__':
    application.run(debug = True)
