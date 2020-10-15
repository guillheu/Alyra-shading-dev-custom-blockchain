import json
from flask import Flask, request
import requests



list_content=[]
app = Flask(__name__)


@app.route('/')
def index():
    return str(list_content)

def set_list_content(list_cntnt):
    list_content = list_cntnt

def start_server():
    app.run()
