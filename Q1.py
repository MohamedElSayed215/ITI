##Q1: Stateful Login Monitor
logins = [ 
    ("ahmed", "success"), 
    ("root", "fail"), 
    ("root", "fail"), 
    ("root", "fail"), 
    ("sara", "success"), 
    ("root", "fail"), 
    ("ahmed", "fail") 
]
user_list=[]
failures=[]

def alert():
    for username , state  in logins :    
        if username  not in user_list :
            failures.append(0)
            user_list.append(username)
        if state == 'fail' :
            failures[user_list.index(username)]+=1    
    for i in range (len(failures)):
        if failures[i] >= 3 :
            print(f'{user_list[i]}  3 failed attempts')



alert()
