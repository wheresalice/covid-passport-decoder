from flask import Flask, send_from_directory, request

import base45
import zlib
from cose.messages import CoseMessage
import cbor


app = Flask(__name__, static_url_path='')


@app.route("/")
def hello_world():
    return send_from_directory('public_html', 'index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('public_html/js', path)


@app.route('/decode', methods=['POST'])
def decode():
    code = request.data.decode("utf-8")
    print(code)

    stripped = code.split("HC1:")[1]
    try:
        base45_decoded = base45.b45decode(stripped)
    except ValueError:
        return '{"error": "invalid base45 string"}'
    zlib_decompressed = zlib.decompress(base45_decoded)
    cose_decoded = CoseMessage.decode(zlib_decompressed)
    cbor_payload = cbor.loads(cose_decoded.payload)
    return cbor_payload


if __name__ == "__main__":
    app.run()
