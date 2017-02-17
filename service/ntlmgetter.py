#! /usr/bin/env python
import os

import requests
from flask import Flask, Response
from requests_ntlm import HttpNtlmAuth

from service import logger

rootlogger= logger.Logger()
url=os.environ.get('url')
user=os.environ.get('username')
password=os.environ.get('password')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    rootlogger.info('Fetching data from '+ url)
    response = requests.get(url,
                 auth=HttpNtlmAuth(user, password))
    if response.status_code == 200:
        # TODO should verify that response is valid json
        rootlogger.info("Receiving data" )
        return Response(response.text, status=response.status_code, mimetype='json')
    else:
        rootlogger.error("ntlm-source returned a non OK http code:")
        # TODO is the response really json here?
        return Response(response.raw, status=response.status_code, mimetype="json")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('port', 5001))
