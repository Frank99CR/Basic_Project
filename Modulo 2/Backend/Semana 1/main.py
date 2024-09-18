from flask import Flask, request, jsonify
import json


app = Flask(__name__)

statuses = ["Not Started", "In Progress", "Completed"]


def open_task_file(path):  
    with open(path, 'r') as file:
        data = json.load(file)
        #print(data)
    return data    



def getSpecificTask(titleTask):  

    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"
    

    existing_tasks = open_task_file(path)
    title_found = None
    for title in existing_tasks:
        if title["Title"] == titleTask:
            title_found = title
        
    return title_found

   

def getSpecificTaskbyId(taskId):  
    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"

    existing_tasks = open_task_file(path)
    task_found = None
    for task in existing_tasks:
        if task["Id"] == int(taskId):
            task_found = task
        
    return task_found



def getAllTask():
    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"

    existing_tasks = open_task_file(path)  

    return existing_tasks
  
       

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

@app.route("/All")  #Listo 100%
def getAllTasks():
    existing_tasks = getAllTask()

    return jsonify(existing_tasks)



@app.route("/create", methods=["POST"])  #Listo 100%
def createTasks():

    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"

    existing_tasks = open_task_file(path)

    new_task_id = request.json['Id']
    new_task_title = request.json['Title'].strip()
    new_task_description = request.json['Description'].strip()
    new_task_status = request.json['Status'].strip()

    for task in existing_tasks:
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
       
    # tasks.append(new_task)
    existing_tasks.append(new_task)
    existing_tasks_converted_to_json = json.dumps(existing_tasks)

    with open (path, 'w') as file:
        file.writelines(existing_tasks_converted_to_json)

    return (existing_tasks_converted_to_json), 201


@app.route("/update/<taskName>", methods=["PUT"])
def updateTasks(taskName):
    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"
    existing_tasks = open_task_file(path)

    task_to_update = getSpecificTask(taskName)
    if not task_to_update:
        return jsonify({"error": "No task found"}), 404
    

    new_Id = request.json.get('Id', task_to_update['Id'])
    new_title = request.json.get('Title', task_to_update['Title']).strip()
    new_description = request.json.get('Description', task_to_update['Description']).strip()
    new_status = request.json.get('Status', task_to_update['Status']).strip()

   
    if new_Id != task_to_update['Id']:
        return jsonify({"Error": "ID cannot be changed"}), 400

 
    validationResponse = validateBlankSpaces(new_title, new_description, new_status)    
    if validationResponse:
        return validationResponse
    
    statusResponse = validateStatuses(new_status)
    if statusResponse:
        return statusResponse

    task_to_update['Title'] = new_title
    task_to_update['Description'] = new_description
    task_to_update['Status'] = new_status

    for index, task in enumerate(existing_tasks):
        if task['Id'] == task_to_update['Id']:
            existing_tasks[index] = task_to_update
            break

    with open(path, 'w') as file:
        json.dump(existing_tasks, file)

    return jsonify(task_to_update), 200



@app.route("/delete/<taskId>", methods=["DELETE"])
def deleteTasks(taskId):
    path = "Modulo 2/Backend/Semana 1/Files/tasks.json"
    existing_tasks = open_task_file(path)

    task_to_delete = getSpecificTaskbyId(taskId)
    if not task_to_delete:
        return jsonify({"error": "No task found"}), 404
    

    tasks= [task for task in existing_tasks if task["Id"] != int(taskId)]
    tasks_converted_to_json = json.dumps(tasks)

    with open (path, 'w') as file:
        file.writelines(tasks_converted_to_json)


    return jsonify({"message": "Task deleted successfully"}), 200



if __name__ == "__main__":
    app.run(host="localhost", port=5003,  debug=True)
