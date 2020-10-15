import json
from flask import Flask, request
import requests
from Blockchain import *
from Block import *

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
        return "could not find block with index \"" + index + "\"\nEither this is not a valid integer, or the index is negative, or that block index has not been added to the chain yet."


app.run()
