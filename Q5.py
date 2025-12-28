processes = [ 
    ("nginx", 30), 
    ("python", 95), 
    ("mysql", 85), 
    ("redis", 20), 
    ("python", 90) 
] 
report={}
def task_manager():
    for service , use  in processes :
        report[service]=0
    for service , use  in processes :
        report[service]+=use
    print(report)    

def alert():
    for  name , usage  in report.items() :
        if usage > 100 :
            print(f'{name} is exceed the limit with usage = {usage}')
            print('Alert !')        
task_manager()
alert()