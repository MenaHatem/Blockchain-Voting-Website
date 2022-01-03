Introduction

This e-voting system is a blockchain-based one. The website lets you choose one of three famous singers to vote for. Blockchains are used as a method of implementing higher security to a transaction or process. This is done by saving the results of the process, saving the vote chosen by each user in our code, using an algorithm that prevents attackers from being able to tamper with the saved data. Being immutable, once a data is saved into a block, it cannot be changed; and, added to it, is a timestamp to ensure verification of the block. For a blockchain to be built, a genesis block is created at first as it is the initial block. The whole idea around the blockchain revolves mainly around hashing the data then manipulating the timestamp and a field named nonce. The nonce is iterated through between zero and about four billion; and the timestamp changes every second between 1/1/1970 till its assigned value. This changes the entire hash, making it hard for an attacker to trace back the actual value that was hashed in the first place.


Instructions

The following are the libraries imported in each file.

database.py & test.py
from sqlite3 import *

program.py
from blockchain import *  (blockchain file included in the folder)
from sqlite3 import *
from flask import *

blockchain.py
from datetime import datetime
from hashlib import sha256
from json import dumps


Flask Installation

Flask is a software used to help in linking python code with web interface. To install it on Windows 10 with python 3, a separate directory is needed which is created by typing the following commands in the cmd.
•	mkdir <project name>
•	cd <project name>

Flask operates in an environment; so, to create one on your device the following commands are also typed in the cmd. It is then activated.
•	py -3 -m venv <name of environment>
•	dir *<project name>*
•	<name of environment>\Scripts\activate

Flask itself is then installed by typing the following:
•	pip install Flask

To test if Flask actually works or not, this simple code is saved in a .py file in any editor and run.
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
return 'Hello world!'

Notes:
To be able to style html files in Flask, the CSS has to be internal. This means that a <style> tag in opened in the head of the html file; as shown below. They should also be added inside a “Template” file as a subfolder to the original folder.

