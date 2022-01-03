from datetime import datetime
from hashlib import sha256
from json import dumps

class blockchain:

    ##creates the first chain##
    def __init__(self):

        self.chain = []
        self.create_block(proof=1 , prev_hash="0")

    ##creates the first block##
    def create_block(self,proof,prev_hash):

        block = { 

            "index":         len(self.chain) + 1 ,
            "timestamp":     str(datetime.now()) ,
            "proof":         proof               , 
            "previous hash": prev_hash

        }

        self.chain.append(block)
        return block

    ##prints the last chain##
    def print_prev_block(self):

        return self.chain[-1]

    ##hashes the current chain##
    def proof_of_work(self,prev_proof):

        new_proof = 1
        check_proof = False

        while check_proof is False:

            hash_operation = sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()

            if hash_operation[:4] == "0000":

                check_proof = True

            else:

                new_proof = new_proof + 1

        return new_proof

    ##hashes the entire block##
    def hash(self,block):
        
        encoded_block = dumps(block,sort_keys=True).encode()

        return sha256(encoded_block).hexdigest()

    ##checks the validity of the chain##
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

            if hash_operation[:4] != "0000":

                return False

            prev_block = block
            block_index = block_index + 1

        return True