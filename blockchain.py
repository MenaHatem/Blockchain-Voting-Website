from datetime import datetime
from hashlib import sha256
from json import dumps
from flask import *

class blockchain:

    def __init__(self):

        self.chain = []
        self.create_block(proof=1 , prev_hash="0")

    def create_block(self,proof,prev_hash):

        block = { 

            "index":         len(self.chain) + 1 ,
            "timestamp":     str(datetime.now()) ,
            "proof":         proof               , 
            "previous hash": prev_hash

        }

        self.chain.append(block)
        return block

    def print_prev_block(self):

        return self.chain[-1]

    def proof_of_work(self,prev_proof):

        new_proof = 1
        check_proof = False

        while check_proof is False:

            hash_operation = sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()

            if hash_operation[:4] == "00000":

                check_proof = True

            else:

                new_proof = new_proof + 1

        return new_proof

    def hash(self,block):
        
        encoded_block = dumps(block,sort_keys=True).encode()

        return sha256(encoded_block).hexdigest()

    def check_chain(self,chain):

        prev_block = chain[0]
        block_index = 1

        while block_index < len(chain):

            block = chain[block_index]

            if block["previous hash"] != self.hash(prev_block):

                return False

            prev_proof = prev_block["proof"]
            proof = block["proof"]
            hash_operation = sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()

            if hash_operation[:4] != "00000":

                return False

            prev_block = block
            block_index = block_index + 1

        return True

# app = Flask(__name__)
# bc = blockchain()

# @app.route('/mine_block', methods=['GET'])
# def mine_block():
#     previous_block = bc.print_prev_block()
#     previous_proof = previous_block['proof']
#     proof = bc.proof_of_work(previous_proof)
#     previous_hash = bc.hash(previous_block)
#     block = bc.create_block(proof, previous_hash)
    
    
     
#     return block
 
# # Display blockchain in json format
# @app.route('/get_chain', methods=['GET'])
# def display_chain():
#     response = {'chain': bc.chain,
#                 'length': len(bc.chain)}
#     return jsonify(response), 200
 
# # Check validity of blockchain
# @app.route('/valid', methods=['GET'])
# def valid():
#     valid = bc.check_chain(bc.chain)
     
#     if valid:
#         response = {'message': 'The Blockchain is valid.'}
#     else:
#         response = {'message': 'The Blockchain is not valid.'}
#     return jsonify(response), 200
 
 
# if __name__ == "__main__":
#     app.run(debug=True)