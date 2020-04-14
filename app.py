import hashlib
import json

blockchain = []

def generateHash(file):
    #read file and create a hash
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open('./Files/'+file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb)>0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    data = file_hash.hexdigest()
    return(data)

def generateBlock(previousHash,file):
    data = generateHash(file)

    #create the block with 
    dic = {'data':data,'previousHash':previousHash}
    dic_package = json.dumps(dic).encode()
    Hash = hashlib.sha256(dic_package).hexdigest()
    block = {'Hash':Hash,'data':data, 'name':file, 'previousHash':previousHash}
    return block

#main
fileName = input('')


#first block
genesisBlock = generateBlock(0,'doc1.odt')
blockchain.append(genesisBlock)

#second block
secondBlock = generateBlock(genesisBlock.get('Hash'),'doc2.odt')
blockchain.append(secondBlock)

#show block chain
print(blockchain)