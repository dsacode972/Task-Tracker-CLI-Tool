#Task Tracker : Class Taasks for prototyping the tasks that have status completed in progress and not completed
import datetime
class Tasks:
    def __init__(self,id,description,status,createdAt,updatedAt):
        self.id=id
        self.description=description
        self.status=status
        self.createdAt=createdAt
        self.updatedAt=updatedAt
    
#update the tasks whenever 