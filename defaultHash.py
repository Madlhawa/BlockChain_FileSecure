import hashlib
import json
data = 'I am gonna be hashed'
data_package = json.dumps(data).encode('utf-8')
Hash = hashlib.sha256(data_package).hexdigest()
print(Hash)