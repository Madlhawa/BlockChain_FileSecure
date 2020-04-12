import hashlib
import json
blockchain = []
def generateBlock(previousHash,data):
    dic = {'data':data,'previousHash':previousHash}
    dic_package = json.dumps(dic).encode()
    Hash = hashlib.sha256(dic_package).hexdigest()
    block = {'Hash':Hash,'data':data,'previousHash':previousHash}
    return block
genesisBlock = generateBlock(0,'I am the first block!')
blockchain.append(genesisBlock)
secondBlock = generateBlock(genesisBlock.get('Hash'),'I am the second block!')
blockchain.append(secondBlock)
print(blockchain)