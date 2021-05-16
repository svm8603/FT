from flask import Flask, request
import json
import logging


logging.basicConfig(filename='server.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

app = Flask(__name__)

# handler = logging.FileHandler("server.log")
# app.logger.addHandler(handler)
# app.logger.setLevel(logging.INFO)

response_api1 = {'response' : 'hello from api1'}
response_api2 = {'response' : 'hello from api2'}

@app.route('/api1', methods=['GET'])
def api1():
    return json.dumps(response_api1)

@app.route('/api2', methods=['POST'])
def api2():
    app.logger.info('json from api2 : {}'.format(request.get_json()))
    return json.dumps(response_api2)