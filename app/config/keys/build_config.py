import json
from jwcrypto.jwk import JWK
from Crypto.PublicKey import RSA

def export_key(filename,key):
    f = open(f"app/config/keys/{filename}", "a")
    f.write(key)
    f.close()
    
    
key = RSA.generate(4096)
private_key = key.exportKey()
print(str(private_key))
export_key('private.key', str(private_key, encoding='UTF-8'))
public_key = key.publickey().exportKey()
print(str(public_key))
export_key('public.key', str(public_key, encoding='UTF-8'))

f = open("app/config/keys/public.key", "r")
public_pem = f.read()
f.close()

jwk_obj = JWK.from_pem(public_pem.encode('utf-8'))
public_jwk = json.loads(jwk_obj.export_public())
public_jwk['alg'] = 'RS256'
public_jwk['use'] = 'sig'
public_jwk_str = json.dumps(public_jwk)

export_key('public.jwk.json', public_jwk_str)

print(public_jwk_str)


    
