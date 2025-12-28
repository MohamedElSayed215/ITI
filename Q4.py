commands = [ 
    ("ls", 0), 
    ("mkdir test", 0), 
    ("rm important.txt", 1), 
    ("cp file1 file2", 0) 
]
cmd=[] 
failures=[]
def cmd_status():
    for command , state  in commands :    
        if command  not in cmd :
            failures.append(0)
            cmd.append(command)
        if state != 0 :
            failures[cmd.index(command)]+=1    
   
    print(cmd)
    print(failures)
cmd_status()    