from Block import *
from Blockchain import *
from Mine import *
import time
import json
import sys
import Flask_server

file = "Blockchain.json"

blockchain = Blockchain(file)
Flask_server.list_content = blockchain.toJson()
print(Flask_server.list_content)
Flask_server.start_server()
