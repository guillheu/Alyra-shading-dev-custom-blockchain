import json
from flask import Flask, request
import requests
from Blockchain import *
from Block import *

BCFile = "Blockchain.json"

app = Flask(__name__)
blockchain = Blockchain(BCFile)

@app.route('/')
def index():
    return str(blockchain.toJson())



app.run()
