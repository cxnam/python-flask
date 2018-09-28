from flask import Flask, jsonify, request
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def get_header():
  default = {"Client IP": "0.0.0.0", "Host": "", "User-Agent": "",
             "Accept": ""}
  try:
    r = request.headers.__dict__
        #print r
    logging.debug("%s"%(r))
    default[u'Client IP'] = request.remote_addr
    default[u'User-Agent'] = r[u'environ'][u'HTTP_USER_AGENT']
    default[u'Host'] = r[u'environ'][u'HTTP_HOST']
    default[u'Accept'] = r[u'environ'][u'HTTP_ACCEPT']
  except:
    pass
  return jsonify(default)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5200)
