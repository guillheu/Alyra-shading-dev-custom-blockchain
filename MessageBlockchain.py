from MessageBlock import *
from json import JSONEncoder
import json
from ConfigHandler import *

#Shamelessly copy-pasted from https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/


class MessageBlockchain:
    def __init__(self, blockchainFile):

        self.chain = []
        try:
            self.loadFromJson(blockchainFile)
        except Exception as e:
            print("Failed to load " + blockchainFile + " : " + str(e))
            self.create_genesis_block()


    def create_genesis_block(self):

        genesis_block = MessageBlock("", "admin", "This is the beginning of this conversation !", time.time())
        self.add(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add(self, block):
        if block.isCorrect:
            self.chain.append(block)








            #Json methods

    def fromJson(self, jsonString):
        for blkTmpl in json.loads(jsonString):
            print(blkTmpl)
            tmp = MessageBlock(blkTmpl['prevHash'], blkTmpl['author'], blkTmpl['message'], blkTmpl['timestamp'])
            tmp.nonce = int(blkTmpl['nonce'], 16)
            self.add(tmp)

    def toJson(self):
        r = "["
        for block in self.chain:
            r += block.toJson()
            r += ","
        r = list(r)
        r[-1] = "]"
        return "".join(r)


    def saveToJson(self, outputFile):
        with open(outputFile, 'w') as blkchn_file:
            blkchn_file.write(self.toJson())

    def loadFromJson(self, inputFile):
        self.fromJson(open(inputFile, 'r').read())


        #Doesnt work properly. Blocks themselves arent prettified
    @property
    def prettyJson(self):
        self.toJson().dumps(parsed, indent=4)
