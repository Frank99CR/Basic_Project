from flask import Flask, request, jsonify


app = Flask(__name__)

tasks = [
    {
        "Id" : 101,
        "Title" : "Code everyday",
        "Description" : "Practice JS & Python",
        "Status" : "Not started",

    },
      {
        "Id" : 102,
        "Title" : "Workout everyday for a month",
        "Description" : "Run 1 mile everyday",
        "Status" : "In progress",

    },

    {
        "Id" : 103,
        "Title" : "Test",
        "Description" : "Testing Flask",
        "Status" : "In progress",

    },

     {
        "Id" : 104,
        "Title" : "Read a book",
        "Description" : "Reading a book",
        "Status" : "Completed",

    },

]

statuses = ["Not Started", "In Progress", "Completed"]

def getSpecificTask(titleTask):
    for title in tasks:
        if title["Title"] == titleTask:
            return title
        
    return "No task found"

def getSpecificTaskbyId(taskId):
    for task in tasks:
        if task["Id"] == int(taskId):
            return task
        
    return None



def getAllTask():
    return tasks

def validateBlankSpaces(new_task_title, new_task_description, new_task_status):
     if not (new_task_title and new_task_description and new_task_status):
        return jsonify({"Error": "Attributes cannot be blank or contain only spaces"}), 400
     return None 

def validateStatuses(new_task_status):
     if new_task_status.lower() not in [status.lower() for status in statuses]:
        return jsonify({"Error": "Please enter a valid status"})
     return None

    
    

@app.route("/Tasks/<taskName>")
def getOneTask(taskName):
    task = getSpecificTask(taskName)
    if task:
        return jsonify(task)
    else:
        return jsonify({"error": "No task found"}), 404

@app.route("/All")
def getAllTasks():
    return jsonify(tasks)



@app.route("/create", methods=["POST"])
def createTasks():
    new_task_id = request.json['Id']
    new_task_title = request.json['Title'].strip()
    new_task_description = request.json['Description'].strip()
    new_task_status = request.json['Status'].strip()

    for task in tasks:
        if task["Id"] == new_task_id:
            return jsonify({"Error ": "ID already used, Please use a different ID"}), 400
        
    validationResponse = validateBlankSpaces(new_task_title, new_task_description, new_task_status)    
    if validationResponse:
        return validationResponse

    statusResponse = validateStatuses(new_task_status)
    if statusResponse:
        return statusResponse

    new_task = {
        "Id" : new_task_id,
        "Title" : new_task_title,
        "Description" : new_task_description,
        "Status" : new_task_status,
    }
       
    tasks.append(new_task)

    return jsonify(tasks), 201



@app.route("/update/<taskName>", methods=["PUT"])
def updateTasks(taskName):

    task_to_update = getSpecificTask(taskName)
    if not task_to_update:
        return jsonify({"error": "No task found"}), 404
    
    new_Id = request.json.get('Id', task_to_update['Id'])
    new_title = request.json.get('Title', task_to_update['Title']).strip()
    new_description = request.json.get('Description', task_to_update['Description']).strip()
    new_status = request.json.get('Status', task_to_update['Status']).strip()

    if new_Id:
        return jsonify({"Error" : "ID cannot be changed"}), 200


    validationResponse = validateBlankSpaces(new_title, new_description, new_status)    
    if validationResponse:
        return validationResponse
    
    statusResponse = validateStatuses(new_status)
    if statusResponse:
        return statusResponse


    task_to_update['Title'] = new_title
    task_to_update['Description'] = new_description
    task_to_update['Status'] = new_status

    return jsonify(task_to_update)

   


@app.route("/delete/<taskId>", methods=["DELETE"])
def deleteTasks(taskId):
    task_to_delete = getSpecificTaskbyId(taskId)
    if not task_to_delete:
        return jsonify({"error": "No task found"}), 404
    
    global tasks
    tasks = [task for task in tasks if task["Id"] != int(taskId)]

    return jsonify({"message": "Task deleted successfully"}), 200



if __name__ == "__main__":
    app.run(host="localhost", port=5003,  debug=True)
