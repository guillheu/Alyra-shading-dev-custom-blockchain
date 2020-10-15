import json
from flask import Flask, request
import requests
from Blockchain import *
from Block import *
from Mine import *

BCFile = "Blockchain.json"

app = Flask(__name__)
blockchain = Blockchain(BCFile)


@app.route('/', methods=['GET'])
def index():
    return str(blockchain.toJson())
@app.route('/block/<index>', methods=["GET"])
def getBlock(index):
    try:
        return blockchain.chain[int(index)].toJson()
    except:
        return "could not find block with index \"" + index + "\"\nEither this is not a valid integer, or the index is negative, or that block index has not been added to the chain yet.", 404

@app.route('/new_message', methods=['POST'])
def addMessage():
    if not request.json:
        return "bad request, no json", 400
    if not 'message' in request.json:
        return "bad request, no message field", 400

    new_block = Block(len(blockchain.chain), blockchain.last_block.hash, request.json['message'], time.time())
    mine(new_block)
    blockchain.add(new_block)
    blockchain.saveToJson(BCFile)


    return "Thank you, your message \"" + json.dumps(request.json["message"]) + "\" has been successfully mined and added to the Blockchain!"



app.run()
