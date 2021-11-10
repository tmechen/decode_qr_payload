import base64

import cwa_pb2

luca_payload = f"$PAYLOAD"

luca_b64_decoded = base64.urlsafe_b64decode(luca_payload)

message = cwa_pb2.QRCodePayload()
message.ParseFromString(luca_b64_decoded)
print(message)
