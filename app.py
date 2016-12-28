import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'consumer_key: ' + os.environ['CONSUMER_KEY']

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

