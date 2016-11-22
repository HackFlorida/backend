
from flask import Flask, url_for, request, jsonify
from datetime import datetime

#need run flask with following command
#flask run --host=0.0.0.0
#need to access http://162.243.15.139:5000/ to get response

app = Flask(__name__)


#NOT INCLUDED IN ITERATION - FUNC

@app.route('/hackget',methods=['GET'])
def getsome():
    info = request.args.get('test')
    return str(info)

@app.route('/hackpost',methods=['POST'])
def postsome():
    info = request.form('test')
    return str(info)

@app.route('/hackjson',methods=['GET'])
def getjson():
    info = "ANDREW IS THE MAN!"
    num = 12
    return jsonify(info = info, num = num)

#Run App
if __name__ == "__main__":
    app.run(host='0.0.0.0')
