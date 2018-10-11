class Todo():
    def __init__(self):
        self.todo_list = []
        """ Delcaring an empty list in this case."""

        
    def add_task (self, name, created_at):

        task = {
            'id': len(self.tod_list) + 1,
            'name': name,
            'created_at': created_at
        }

        self.todo_list.append(task)
        return self.todo_list

    def show_tasks(self):
        return self.todo_list

    def delete_task(self, name):
        self.todo_list.pop()
        return self.todo_list


   


    

