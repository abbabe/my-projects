from email import message
from unicodedata import name
from flask import Flask, render_template

# object name
app=Flask(__name__)



@app.route("/")

def head(): 
    strMessage="This is my first conditions experience"
   
    return render_template("index.html",message=strMessage)


@app.route("/list")

def header():

    names =["Ayhan", "Ertugrul", "Irem"]
    
    return render_template("body.html", object = names)

    # run this app in debug mode on your local.

if __name__== "__main__":
    app.run(debug=True)