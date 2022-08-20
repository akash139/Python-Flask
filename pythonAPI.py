from flask import Flask, jsonify, request
app = Flask(__name__)

employee = [{'Name': 'Akash',
             'Emp_Id': '10001',
             'Team': 'Automation',
             'Designation': 'Software Engineer',
             'Location': 'Bangalore'
             },
            {'Name': 'Rahul',
             'Emp_Id': '10002',
             'Team': 'Automation',
             'Designation': 'Bussiness Analyst',
             'Location': 'Mumbai'
             },
            {'Name': 'Zeesha',
             'Emp_Id': '10003',
             'Team': 'Automation',
             'Designation': 'Sales Executive',
             'Location': 'Delhi'
             },
            {'Name': 'Preeti',
             'Emp_Id': '10004',
             'Team': 'Automation',
             'Designation': 'Human Resource',
             'Location': 'Bangalore'
             }
            ]

## Home Page
@app.route('/')
def home():
    return "Welcome to the home page."

## GET Response
# @app.route('/employee/', methods=['GET'])
# def getEmployee():
#     return jsonify({'Employee_Details': employee})

## GET using specfic emp_Id
@app.route('/employee/<int:Emp_Id>', methods=['GET'])
def getSpecificEmployee(Emp_Id):
    for item in range(0, len(employee)-1):
        if str(Emp_Id) == employee[item]['Emp_Id']:
            return jsonify({ 'Employee_Details': employee[item] })
    return jsonify({'Employee_Details': 'Employee Not Found!'})


# GET using specific emp_Name
@app.route('/employee/<string:Name>', methods=['GET'])
def getSpecificEmployeeWithName(Name):
    for item in employee:
        if str(Name).lower() == item['Name'].lower():
            return jsonify({'Name': item['Name'], 'Emp_Id': item['Emp_Id'], 'Team': item['Team'], 'Designation': item['Designation'], 'Location': item['Location']})
    return jsonify({'Employee_Details': 'Employee Not Found!'})

## Static Post Response
# @app.route('/employee/', methods=['POST'])
# def addEmployee():
#     addedEmp = {'Name': 'Rakesh',
#                 'Emp_Id': '100',
#                 'Team': 'Automation',
#                 'Designation': 'Software Engineer',
#                 'Location': 'Bangalore'
#                 }
#     employee.append(addedEmp)
#     return jsonify({'Employee_Details': employee})

## Dyanmic [GET/POST] Response
@app.route('/employee/', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST' and request.json not in employee:
        employee.append(request.json)
        return jsonify({'Employee_Details': employee})
    elif request.method == 'GET':
        return jsonify({'Employee_Details': employee})
    else:
        return jsonify({'Employee_Details': 'Employee Already Exists.'})

## PUT Response //Update
@app.route('/employee/<int:Emp_Id>/<string:name>', methods=['PUT'])
def updateEmployee(Emp_Id, name):
    for item in employee:
        if request.method == 'PUT' and str(Emp_Id) == item['Emp_Id']:
            item['Name'] = name
            return jsonify({'Employee_Details': employee})
    return jsonify({'Employee_Details': 'Employee Not Found!'})
        
## DELETE Employee
@app.route('/employee/<int:id>', methods=['DELETE'])
def removeEmp(id):
    for item in range(0, len(employee)-1):
        if str(id) == employee[item]['Emp_Id']:
            employee.remove(employee[item])
            return jsonify({'Employee_Details': employee})
    return jsonify({'Employee_Details': 'Employee Not Found!'})

if __name__ == '__main__':
    app.run(debug=True)
