from Block import *
from json import JSONEncoder
import json

#Shamelessly copy-pasted from https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/


class Blockchain:



    def __init__(self, blockchainFile):
        """
        Constructor for the `Blockchain` class.
        """
        self.chain = []
        try:
            self.loadFromJson(blockchainFile)
        except Exception as e:
            print("Failed to load " + blockchainFile + " : " + str(e))
            self.create_genesis_block()


    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, "", {"name":"Brice","come from":"Nice","surfer":"Winner","ascendant":"Snowboarder","king of":"La Glisse","manual needed":False,"Other surfaces":"Le roi de la Casse"}, "0")
        genesis_block.hash = genesis_block.hash
        self.add(genesis_block)

    @property
    def last_block(self):
        """
        A quick pythonic way to retrieve the most recent block in the chain. Note that
        the chain will always consist of at least one block (i.e., genesis block)
        """
        return self.chain[-1]

    def add(self, block):
        if block.isCorrect:
            self.chain.append(block)





            #Json methods

    def fromJson(self, jsonString):
        for blkTmpl in json.loads(jsonString):
            print(blkTmpl)
            tmp = Block(blkTmpl['index'], blkTmpl['prevHash'], blkTmpl['data'], blkTmpl['timestamp'])
            tmp.salt = blkTmpl['salt']
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
