import json
def store_in_json():
    dic_data = {      
    "name": "Alice", 
    "age": 25, 
    "city": "New York"     
            }
    try :
        # Write     
        json_file=open('data.json', 'w') 
        json.dump(dic_data, json_file)
        # Read
        json_file=open('data.json', 'r') 
    except IOError : 
        print("please don't write at this file")    
    else : 
        print(json.load(json_file))
    
store_in_json()