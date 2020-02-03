from flask import Flask
from flask import jsonify

app = Flask(__name__)

APP_VERSION = 4.0

@app.route('/')
def hello_world():
    return 'Hello, My name is Michael and I Like AI and ML!'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
