
from flask import Flask
app = Flask(__name__)



strHomeMessage= "Hello, Flask!, Hello Galaxy, I succeed it :) "
strSecondMessage="This is second page "
strThirdMessage ="This is the subpage of third page"

@app.route("/")
def home():
    return strHomeMessage


@app.route('/second')
def second ():
    return strSecondMessage
    

@app.route('/third/subthird')
def third ():
    return strThirdMessage


@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'



if __name__ == "__main__":
    app.run(debug=True, port=3000)



