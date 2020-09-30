from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>Lab OpenShift</h1><p>Hola, Tepic!</p>x\r\n", 200, { 'Content-Type': 'text/plain' }

if __name__ == '__main__':
    application.run(debug = True)
