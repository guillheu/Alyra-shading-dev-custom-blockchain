from Block import *
from Blockchain import *
from Mine import *
import time
import json

file = "Blockchain.json"

blockchain = Blockchain(file)
lb = blockchain.last_block
new_block = Block(lb.index+1, lb.hash, ["a block content"], time.time())
mine(new_block)
blockchain.add(new_block)
blockchain.saveToJson(file)
