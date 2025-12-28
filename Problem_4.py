from pathlib import Path 
import json
def reading_file():
    input_file=input('Enter file name : ')
    file=Path(input_file)
    try :
        content=file.read_text()
    except FileNotFoundError :
        print(f"file name : '{file}' is not exist")
        text=input('Would you like to try again? (yes/no):')
        if text == 'yes' :
            reading_file()
    else :       
        print(content)

def write_data():
    input_file=input('Enter file name : ')
    text=input('Enter text to save ')
    file=Path(input_file)
    try :
        file.write_text(text)
    except PermissionError :
        print(f"file name : '{file}' can not write !")
    else :       
        print(file.read_text())

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
while True : 
    print('Main Menu \n1. Read a file \n2. Write to a file \n3. Save data to JSON \n4. Exit')
    usr_input=input()
    if usr_input == '1' :
        reading_file()
    elif  usr_input == '2':
        write_data()
    elif  usr_input == '3':
        store_in_json()
    elif  usr_input == '4':
        print('Exit !!')
        break 