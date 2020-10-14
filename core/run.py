from Block import *
from Blockchain import *
from Mine import *
import time
import json
import sys

file = "Blockchain.json"

blockchain = Blockchain(file)

print(sys.version)
