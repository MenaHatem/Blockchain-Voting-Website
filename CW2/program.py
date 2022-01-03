from blockchain import *
from sqlite3 import *
from flask import *

##a connection to flask is made##
app = Flask(__name__)

##a connection to the database is made## 
##check_same_thread is used to ensure that multiple users can add data without its corruption##
conn = connect("database.db" , check_same_thread=False)

##the blockchain class is imported from its file and assigned into a variable##
BC = blockchain()

##this decorator is used to route the user upon running the program to a certain webpage##
@app.route("/")
def start():

    ##render_template is used to return the webpage we want to be viewed upon running code##
    return render_template("voting.html")

@app.route("/voting" , methods=["POST"])
def voting():

    if request.method == "POST":

        ##these variables are used to extract the data filled in by the user in the html form##
        username = request.form["username"].strip().lower()
        email = request.form["email"].strip().lower()
        vote = request.form["vote"].strip().lower()

        ##a query is created to check if the email entered was entered before or not##
        cursor = conn.execute("SELECT EMAIL from Users")

        try:

            for row in cursor:

                if email != row[0]:
        
                    ##question marks are used to be able to enter data temporarily##
                    ##variables are then specified to denote the question marks##
                    conn.execute("INSERT INTO Users (USERNAME,EMAIL,VOTE) VALUES (?,?,?)" , (username,email,vote))
                    conn.commit()
                                
                    return redirect(url_for("results"))
                   # return redirect(url_for("mine_block"))

        except:

            return "This email voted before"

@app.route("/results")
def results():

    list = []
    singer_1 = 0
    singer_2 = 0
    singer_3 = 0

    ##a query is created to select the vote field from the database##
    cursor2 = conn.execute("SELECT VOTE from Users")
    for column in cursor2:
        
        ##contents of the vote field are added into a list to keep score using singer variables##
        list.extend(column)

    for i in list:

        if i == "the weeknd":

            singer_1 = singer_1 + 1

        elif i == "halsey":

            singer_2 = singer_2 + 1

        elif i == "arctic monkeys":

            singer_3 = singer_3 + 1

    conn.close()

    ##the singer vriables are returned to be able to view their contents in the results.html file##
    return render_template("results.html" , singer_1 = singer_1 , singer_2 = singer_2 , singer_3 = singer_3 )

# @app.route("/mine_block")
# def mine_block():

#     previous_block = BC.print_prev_block()
#     previous_proof = previous_block["proof"]
#     proof = BC.proof_of_work(previous_proof)
#     previous_hash = BC.hash(previous_block)

#     block = BC.create_block(proof,previous_hash)

#     respond = { "message":   "Successfully mined"    ,
#                 "index":      block["index"]         ,
#                 "timestamp":  block["timestamp"]     ,
#                 "proof":      block["proof"]         ,
#                 "prev_hash":  block["previous hash"] }

#     return jsonify(respond) , 200

# @app.route("/get_chain")
# def display_chain():

#     respond = { "chain":  BC.chain      ,
#                 "length": len(BC.chain) }

#     return jsonify(respond), 200
 

# @app.route("/validity")
# def validity():

#     valid = BC.check_chain(BC.chain)
     
#     if valid:

#         respond = {"message": "It is valid"}

#     else:

#         respond = {"message": "It is not valid"}

#     return jsonify(respond), 200

##this is used to avoid running the code after saving##
##instead it automatically applies changes so that the webpage is just refreshed##
if __name__ == "__main__":
    app.run(debug=True)