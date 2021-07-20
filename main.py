import sys
import base45
import zlib
from cose.messages import CoseMessage
import cbor
import json
from datetime import datetime

qr_code = sys.argv[1]

stripped = qr_code.split("HC1:")[1]
base45_decoded = base45.b45decode(stripped)
# print(base45_decoded)

zlib_decompressed = zlib.decompress(base45_decoded)
# print(zlib_decompressed)

cose_decoded = CoseMessage.decode(zlib_decompressed)

# print(cose_decoded.payload)

cbor_payload = cbor.loads(cose_decoded.payload)

claim_names = {1: "Issuer", 6: "Issued At", 4: "Expiration time", -260: "Health claims"}
for k in cbor_payload:
    if k != -260:
        n = f'Claim {k} (unknown)'
        if k in claim_names:
            n = claim_names[k]
        if k == 6 or k == 4:
            ts = int(cbor_payload[k])
            print(f'{n:20}: {datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")}')
        else:
            print(f'{n:20}: {cbor_payload[k]}')

payload = cbor_payload[-260][1]
n = 'Health payload'
print(f'{n:20}: ', end="")

print(json.dumps(payload))
