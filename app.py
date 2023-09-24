## write a simple flask application

from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learning Project today and you will learn a lot. by building projects you will get a good exposure"


if __name__=="__main__":
    app.run(debug=True)

