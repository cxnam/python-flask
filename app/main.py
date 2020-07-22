from flask import Flask, jsonify, request
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def foo():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=80)
