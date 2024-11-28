#Task Tracker : Class Taasks for prototyping the tasks that have status completed in progress and not completed
import json
import cmd
import datetime
import random
class Tasks:
    def __init__(self,id,description,status,createdAt,updatedAt):
        self.id=id
        self.description=description
        self.status=status
        self.createdAt=createdAt
        self.updatedAt=updatedAt
    def to_dict(self):
        return {
            "id":self.id,
            "description":self.description,
            "status":self.status,
            "createdAt":self.createdAt,
            "updatedAt":self.updatedAt
        }
        
        
class TaskTracker(cmd.Cmd):
    prompt='task-cli>>'
    intro='Welcome to Task Tracker - a tool that helps you control and monitor your tasks'
    
    def __init__(self):
        super().__init__()
        self.task_list={}
    
    def do_add(self,task):
        #Adding products like add "Milk Carton"
        task_id=random.randint(1,1000000)
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_item=Tasks(task_id,task,'undone',time,time)
        self.task_list[task_id]=task_item
        with open("tasklist.json","w") as file:
            json_list={task_id:task.to_dict() for task_id,task in self.task_list.items()}
            file.write(json.dumps(json_list))
        print(f"Task added successfully (ID: {task_id})")
    
    def do_update(self,id,message):
        pass
    
    def do_delete(self,id):
        id=int(id)
        if(id in self.task_list):
            del self.task_list[id]
            with open("tasklist.json","w") as file:
                json_list={task_id:task.to_dict() for task_id,task in self.task_list.items()}
                file.write(json.dumps(json_list))
        else:
            print(f"There is no task with the given ID to be deleted")
    def do_mark(self):
        pass
    
    def do_list(self):
        pass
#update the tasks whenever 

if __name__=='__main__':
    TaskTracker().cmdloop()