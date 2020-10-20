from hashlib import sha256
import json
import time
from json import JSONEncoder
from ConfigHandler import *


class MessageBlock:
    def __init__(self, prevHash, author, message, timestamp):


        self.prevHash = prevHash
        self.author = author
        self.message = message
        self.timestamp = timestamp
        self.nonce = 0

    @property
    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()



    def toJson(self):
        return "{\"prevHash\":\"" + self.prevHash + "\", \"author\":\"" + self.author + "\",\"message\":" + json.dumps(self.message) + ",\"timestamp\":" + str(self.timestamp) + ",\"nonce\":\"" + hex(self.nonce) + "\"}"

        #To be implemented
    @property
    def isCorrect(self):
        return True

    @property
    def prettyJson(self):
        return self.toJson()
