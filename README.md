# cwa_qr_decoder

* install protobuf (https://developers.google.com/protocol-buffers/docs/downloads)
* generate python file from .proto 
```
protoc --python_out=. cwa.proto
```
* replace $PAYLOAD with qr payload
  * https://e.coronawarn.app?v=1#{$PAYLOAD}
  * https://app.luca-app.de/webapp/LUCAWEBAPPIDENTIFIER#e30/CWA1/{$PAYLOAD}

* if padding is incorrect, add '=' to fill base64
* run decode_qr_payload.py
* example output
```
version: 1
locationData {
  version: 1
  description: "DecodingTestLocation"
  address: "11111 Musterstadt"
}
crowdNotifierData {
  version: 1
  publicKey: "\203\002\314\314My\336\3240\000\347\3661\232\024]w\363Y7eJ\227\322\367\330\231}\371\234\233\023\206\366x\322+\204S\212aN\027\000\341\352\335\023\313\017\027GMn\2006#\266\342\260\216;\212\343\323\241\363qVr\336\227\245\347\317\213\324\244\217\033\357\317\235\342\366\006\214\231A\034\367\252[\266\206\200"
  cryptographicSeed: "c\374>\276Qi\013\345\n0\371\364\251\001u{"
}
vendordata {
  version: 1
  type: LOCATION_TYPE_PERMANENT_EDUCATIONAL_INSTITUTION
  defaultCheckInLengthInMinutes: 1425
}


```
