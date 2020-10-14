from hashlib import sha256
import json
import time
from json import JSONEncoder


class Block:
    def __init__(self, index, prevHash, data, timestamp):
        """
        Constructor for the 'Block' class
        """

        self.index = index
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp
        self.salt = 0

    @property
    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()



    def toJson(self):
        return "{\"index\":" + str(self.index) + ",\"prevHash\":\"" + self.prevHash + "\",\"data\":" + json.dumps(self.data) + ",\"timestamp\":" + str(self.timestamp) + ",\"salt\":\"" + hex(self.salt) + "\"}"

        #To be implemented
    @property
    def isCorrect(self):
        return True
