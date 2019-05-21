#!/C/Users/djdav/Development/Python/vending_machine/venv/Scripts/python

from flask import Flask, json
from flask import Response
from flask import request

from src.controller.vending_machine import vending_machine

app = Flask(__name__)


@app.route('/vending_machine/health', methods=['GET'])
def health():
    return Response(status=200)


@app.route('/vending_machine/make_purchase', methods=['POST'])
def make_purchase():
    request_json = json.loads(request.data)
    list_coins = request_json['list_coins']
    product_location = request_json['product_location']
    result = vending_machine(list_coins, product_location)
    return Response(json.dumps(result), status=200)


if __name__ == '__main__':
    app.run(debug=True)
