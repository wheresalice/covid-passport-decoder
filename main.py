import sys
import base45
import zlib
from cose.messages import CoseMessage
import cbor

qr_code = sys.argv[1]

stripped = qr_code.split("HC1:")[1]
base45_decoded = base45.b45decode(stripped)
# print(base45_decoded)

zlib_decompressed = zlib.decompress(base45_decoded)
# print(zlib_decompressed)

cose_decoded = CoseMessage.decode(zlib_decompressed)

# print(cose_decoded.payload)

cbor_payload = cbor.loads(cose_decoded.payload)

print(cbor_payload)
