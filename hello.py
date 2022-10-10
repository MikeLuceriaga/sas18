from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
empDB=[
{
'id':'101',
'name':'Dorry Britz',
'title': 'Technical Leader '
},
{
'id':'102',
'name':'Barbie Gurl',
'title':'Software Engineer '
}
empDB = [
    {
        'id': '101',
        'name': 'Dorry Britz',
        'title': 'Technical Leader',
    },
    {
        'id': '102',
        'name': 'Ice',
        'title': 'Software Engineer',
    }
]


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/empdb/employee/', methods=['GET'])
def getAllEmp():
    return jsonify({'emp':empDB})
    return jsonify({'emp': empDB})


@app.route('/empdb/employee/<empId>', methods=['GET'])
def getEMP(empId):
    usr = [emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp': usr})

@app.route('/empdb/employee/<empID>', methods=['GET'])
def getEmp(empId) :
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    return jsonify({'emp':usr})

if __name__== "__main__":
    app.run()
if __name__ == "__main__":
    app.run()	