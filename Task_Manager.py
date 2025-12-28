class Task:
    def __init__(self,name,done):
        self.name=name 
        self.done=done 
    def get_name(self):
        return self.name 
    def get_status(self):
        return self.done   
    def set_status(self,status):
        self.done=status     
class Task_Manager:
    tasks=[]
    def create_task(self,name,status='false',tasks=tasks):
        task = Task(name,status)
        tasks.append(task) 

    def mark_complete(self,name,tasks=tasks):
        for i in range (len(tasks)) :
            if tasks[i].get_name() == name :
                tasks[i].set_status('true')

    def list_tasks(self,tasks=tasks):
        print('\t---------------')
        print('\tList All Tasks:')
        print('\t---------------')
        for i in range (len(tasks)) : 
            print(f'\tstatus of {tasks[i].get_name()} is {tasks[i].get_status()}')
                       
    def list_pending_tasks(self,tasks=tasks):
        print('\t-------------------')
        print('\tList Pending Tasks:')
        print('\t-------------------')
        for i in range (len(tasks)) :
            if tasks[i].get_status() == 'false' :
                print(f'\t{tasks[i].get_name()}')
        

Manager=Task_Manager()
Manager.create_task('firefox')
Manager.create_task('adobe')
Manager.create_task('vs-code')
Manager.mark_complete('firefox')
Manager.list_tasks()
Manager.list_pending_tasks()