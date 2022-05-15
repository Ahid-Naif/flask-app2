from flask import Flask
from flask import request
import numpy as np
import json

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route("/similar", methods=['POST'])
def similar():
    data = json.loads(request.data)

    result = 50
    # result_file = open("result.txt", "w")
    # result_file.write(str(result))
    # result_file.close()

    return json.dumps({"value": result}, cls=NumpyEncoder)
  
@app.route("/getResult", methods=['get'])
def getResult():
    # result = open("result.txt", "r")
    # result_data = result.read()
    # result.close()

    # result_file = open("result.txt", "w")
    # result_file.write("")
    # result_file.close()

    return "50"

# main driver function
if __name__ == '__main__':
    app.run()