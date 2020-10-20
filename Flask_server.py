import json
from flask import Flask, request
import requests
from MessageBlockchain import *
from MessageBlock import *
from MessageMine import *
from ConfigHandler import *



msgBCFile = getConfigVar('MessageBlockchainFile')
localPort = getConfigVar("Port")
hostAddress = getConfigVar('HostAddress')
HTMLFolder = "html/"
HTMLBlockchainSymbol = "[BLOCKCHAIN]"
HTMLBlockSymbol = "[BLOCK]"


# Contains the host addresses of other participating members of the network
peers = set()

app = Flask(__name__)
messageBlockchain = MessageBlockchain(msgBCFile)


@app.route('/', methods=['GET'])
def index():
    with open(HTMLFolder+"index.html", 'r') as f:
        return f.read().replace(HTMLBlockchainSymbol, str(messageBlockchain.toJson()))
    return str(messageBlockchain.toJson())



@app.route('/block', methods=["GET"])
def getBlock():
    try:
        index = request.args["index"]
        print(index)
        b = messageBlockchain.chain[int(index)].toJson()
        with open(HTMLFolder + "block.html") as f:
            return f.read().replace(HTMLBlockSymbol, b)
    except:
        return "Block not found", 404

@app.route('/new_message', methods=['POST', 'GET'])
def addMessage():
    if request.method=='POST':
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
        msg = request.form["message"]
        author = request.form["author"]


        new_block = MessageBlock(messageBlockchain.last_block.hash, author, msg, time.time())
        mine(new_block)
        messageBlockchain.add(new_block)
        messageBlockchain.saveToJson(msgBCFile)
        with open(HTMLFolder + "new_message_success.html") as f:
            return f.read().replace(HTMLBlockSymbol, messageBlockchain.last_block.toJson())
        return new_block.toJson()
    with open(HTMLFolder + "new_message_form.html") as f:
        return f.read()
    return "internal error", 500


###Consensus functions

# Endpoint to add new peers to the network
@app.route('/register_node', methods=['POST'])
def register_new_peers():
    # The host address to the peer node
    node_address = request.json["node_address"]
    if not node_address:
        return "Invalid data", 400

    # Add the node to the peer list
    peers.add(node_address)

    # Return the blockchain to the newly registered node so that it can sync
    return messageBlockchain.toJson()

def retreive_peers_chain():
    for node in peers:
        response = requests.get(node)
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and messageBlockchain.check_chain_validity(chain):
              # Longer valid chain found!
            current_len = length
            longest_chain = chain








app.run(host=hostAddress, port=localPort)
