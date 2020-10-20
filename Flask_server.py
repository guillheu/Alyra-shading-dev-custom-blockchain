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


# Contains the host addresses of other participating members of the network
peers = set()

app = Flask(__name__)
messageBlockchain = MessageBlockchain(msgBCFile)


@app.route('/', methods=['GET'])
def index():
    return str(messageBlockchain.toJson())



@app.route('/block/<index>', methods=["GET"])
def getBlock(index):
    try:
        return messageBlockchain.chain[int(index)].toJson()
    except:
        return "could not find MessageBlock with index \"" + index + "\"\nEither this is not a valid integer, or the index is negative, or that block index has not been added to the chain yet.", 404

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
        return "Thank you "+author+", your message \"" + msg + "\" has been successfully mined and added to the Blockchain!"
    return """
  <form action="/new_message" method="post">
    <input type="text" name="author"/>
    <input type="text" name="message"/>
    <input type="submit" value="Send your message"/>
    </form>
        """


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
