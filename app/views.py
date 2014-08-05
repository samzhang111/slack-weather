from app import app
import flask
from flask import render_template
from flask import request
from flask import Response
from flask import abort
from flask import jsonify
import json
import os

import re
import requests


slack_url = os.getenv('DSSG_SLACK_URL')

def write_slack(msg, description):
    payload = {
            'text': '''Is the weather weird today?
<http://www.istheweatherweird.com|{msg}>
{desc}'''.format(msg=msg, desc=description)
            }
    print jsonify(payload)
    r = requests.post(slack_url, data = json.dumps(payload))

    return r

@app.route('/receive', methods=['POST'])
def kimono_endpoint():
    print request.data, request.values
    result = json.loads(request.data)['results']['collection1'][0]
    verdict = result['verdict']
    statement = result['statement']
    write_slack(verdict, statement)

    return jsonify({})

@app.route('/')
def root():
    return ''
