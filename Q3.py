disks = { 
    "/": 85, 
    "/home": 70, 
    "/var": 92, 
    "/tmp": 60 
} 

def display_status():
    cleanup_counts=0
    for value in disks.values():
        if value >90 :
            print('CRITICAL cleanup required')
            cleanup_counts+=1
        elif value >80 and value < 90 :
            print('WARNING')
        elif value <80 :
            print('OK') 
    return cleanup_counts        
counts=display_status()               
print(counts)        