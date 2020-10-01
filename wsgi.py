from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h2>Lab OpenShift</h2><p>Hola, Tepic!</p>", 200, { 'Content-Type': 'text/html' }

if __name__ == '__main__':
    application.run(debug = True)
