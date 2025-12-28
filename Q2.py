logs = [ 
    "INFO system boot", 
    "ERROR disk full", 
    "WARNING memory high", 
    "ERROR permission denied", 
    "INFO service started", 
    "WARNING cpu high" 
] 
log_levels=[]
filtered_log_levels=[]
log_counts=[]
for log in logs :
    log_levels.append(log.split()[0])
for log in log_levels :
    if log not in filtered_log_levels :
        filtered_log_levels.append(log)
        log_counts.append(0)      
    log_counts[filtered_log_levels.index(log)]+=1
print(filtered_log_levels)    
print(log_counts)

            