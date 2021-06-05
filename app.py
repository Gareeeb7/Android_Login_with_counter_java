# importing libraries
from flask_restful import Api, Resource
from flask import Flask, jsonify, request
import mysql.connector


mydb = mysql.connector.connect(
  host = "db4free.net",
  user = "tutionmaster",
  password = "tutionmaster",
  database = "tutionmaster"
)

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData:
            return 301 #Missing parameter
        else:
            return 200


class Add(Resource):
    def post(self):
        
        postedData = request.json
        postedData_list = postedData.items()
        user_data = []
        
        for key, value in postedData_list:
            user_data.append(value)
            
        email = user_data[0]
        password = user_data[1]

        #email = "jdhfusi"
        #password = "udhsfuhiu"
        mycursor = mydb.cursor()
        query = f"SELECT Email, Pass FROM Mobile_user where Email = '{email}' AND Pass = '{password}'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            data.append(x)
            
        # Verify validity of posted data
        try:
            if(email == data[0][0] and password == data[0][1]):
                result = "K1S"
                print(result)

            else:
                result = "K0S"
                print(result)
    
        except IndexError:
            result = "K0S"
            print(result)
          
        status_code = 200

        return result


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "API Working fine"


if __name__=="__main__":
    app.run(debug=True)


