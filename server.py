from flask import Flask, request
from flask_cors import CORS
import ddddocr
import base64
from gevent import pywsgi
app = Flask(__name__)
CORS(app)
ocr = ddddocr.DdddOcr(show_ad=False)

@app.route('/')
def hello_world():
    return 'Welcome to the Captcha Server! Post your captcha to /api'

@app.route('/api', methods=['POST'])
def api():
    try:
        captcha = request.form['captcha']
        captcha = base64.b64decode(captcha)
        return ocr.classification(captcha)
    except KeyError:
        return 'Error: No captcha provided', 400


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app, keyfile='xxx.xxx.xxx.xxx-key.pem', certfile='xxx.xxx.xxx.xxx.pem')
    server.serve_forever()
