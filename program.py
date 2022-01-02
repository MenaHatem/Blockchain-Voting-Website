from sqlite3 import *
from flask import *
from pytz import UTC
from datetime import datetime
from hashlib import sha512
from time import sleep

app = Flask(__name__)
conn = connect("database.db" , check_same_thread=False)

@app.route("/")
def start():
    return render_template("register.html")

@app.route("/register" , methods=["POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip().lower()
        email = request.form["email"].strip().lower()
        cursor = conn.execute("SELECT EMAIL from Users")

        try:

            for row in cursor:

                if email != row[0]:

                    conn.execute("INSERT INTO Users (USERNAME,EMAIL) VALUES (?,?)" , (username,email))
                    conn.commit()
                    conn.close()
                    
                    return redirect(url_for('success', name = username))

        except:

            return "an account with the same email already exits"

@app.route("/success")
def success():

    print("You have successfully registered")

    return redirect(url_for("voting"))

@app.route("/voting") 
def voting():

    return redirect(url_for("vote"))

@app.route("/vote" , methods=["GET"]) 
def vote():

    vote = request.get.submit["vote"]
    conn.execute("INSERT INTO Vote (VOTE) VALUES (?)" , (vote))
    conn.commit()

    return "You have successfully added your vote"



if __name__ == "__main__":
    app.run(debug=True)