import hashlib,base58,binascii

# it is not used but it is another way to convert Byte to Hex
def convertByteToHex(inp):
    return ''.join(["%02x" % x for x in inp])

# mypublickey = '1M2tgkBsUeo2XYAjgapENNb2kxH1gzY3VH'

bitcoinAddress = input("Enter a bitcoin address:")
print("--------------------------------------")
print("Bitcoin Address: ", bitcoinAddress)
# base58.b58decode method generate Byte and we should convert it to Hex with hex() method
base58Decoder = base58.b58decode(bitcoinAddress).hex()
print("Base58 Decoder: ", base58Decoder)
prefixAndHash = base58Decoder[:len(base58Decoder)-8]
checksum = base58Decoder[len(base58Decoder)-8:]
print("\t|___> Prefix & Hash: ", prefixAndHash)
print("\t|___> Checksum: ", checksum)
print("--------------------------------------")
# to handle true result, we should pass our input to hashlib.sha256() method() as Byte format
# so we use binascii.unhexlify() method to convert our input from Hex to Byte
# finally, hexdigest() method convert value to human-readable
hash = prefixAndHash
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    print("Hash#", x, " : ", hash)
print("--------------------------------------")
if(checksum == hash[:8]):
    print("[TRUE] checksum is valid!")
else:
    print("[FALSE] checksum is not valid!")
