__author__ = 'dattnguyen82@gmail.com'

import os

from flask import Flask
from flask import request
from flask_cors import cross_origin

app = Flask(__name__)

port = None

### Application Configuration
portStr = os.getenv("VCAP_APP_PORT")

if portStr is not None:
    port = int(portStr)


def print_request(req, label=''):
    print "Label: " + label + os.linesep
    print req.path
    print req.method
    print str(req.data)


@app.route('/get', methods=['GET'])
def get_forecasts():
    response = 'GET OK'
    return response


@app.route('/post', methods=['POST'])
@cross_origin()
def fail():
    response = 'POST OK'
    print_request(request, "fail")
    return response


@app.route('/')
def main():
    response = 'Python - Flask Sample '

    return response

### Main application
if __name__ == '__main__':
    if port is not None:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()